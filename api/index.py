from flask import Flask, request, send_file, jsonify
import sys
import os
import io

# Add the parent directory to sys.path to allow importing lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.cifra_logic import get_cifra_content, generate_pdf_bytes, generate_docx_bytes

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    try:
        print(f"Received request data: {str(data).encode('utf-8', errors='ignore')}", file=sys.stderr)
    except:
        pass
        
    url = data.get('url')
    format_type = data.get('format', 'pdf') # pdf or docx
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
        
    # Strip fragment (e.g. #google_vignette=true)
    target_key_index = None
    if '#' in url:
        parts = url.split('#')
        url = parts[0]
        fragment = parts[1]
        # Parse key=value from fragment
        for param in fragment.split('&'):
            if param.startswith('key='):
                try:
                    target_key_index = int(param.split('=')[1])
                    print(f"DEBUG: Extracted key index from URL: {target_key_index}", file=sys.stderr)
                except:
                    pass

        
    try:
        print(f"Processing URL: {url} with key index: {target_key_index}", file=sys.stderr)
        title, artist, key, lines = get_cifra_content(url, target_key_index)
        
        # Sanitize filename
        safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        safe_artist = "".join([c for c in artist if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        filename = f"{safe_title}_{safe_artist}".replace(" ", "_")
        
        if format_type == 'pdf':
            pdf_bytes = generate_pdf_bytes(title, artist, key, lines)
            return send_file(
                io.BytesIO(pdf_bytes),
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f"{filename}.pdf"
            )
        elif format_type == 'docx':
            docx_bytes = generate_docx_bytes(title, artist, key, lines)
            return send_file(
                io.BytesIO(docx_bytes),
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                as_attachment=True,
                download_name=f"{filename}.docx"
            )
        else:
            return jsonify({"error": "Invalid format"}), 400
            
    except Exception as e:
        print(f"Error processing request: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5328)
