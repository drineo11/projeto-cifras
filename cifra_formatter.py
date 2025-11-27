import sys
import os
from lib.cifra_logic import get_cifra_content, get_content_from_file, generate_pdf_bytes, generate_docx_bytes

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python cifra_formatter.py <URL ou Arquivo.txt>")
        url = "https://www.cifraclub.com.br/isaias-saad/bondade-de-deus/"
        print(f"Usando URL padrão: {url}")
    else:
        url = sys.argv[1]
        if '#' in url:
            url = url.split('#')[0]

    print(f"Processando: {url}")
    
    try:
        if os.path.isfile(url):
            title, artist, key, lines = get_content_from_file(url)
        else:
            title, artist, key, lines = get_cifra_content(url)
        
        # Sanitize filename
        safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        safe_artist = "".join([c for c in artist if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        base_filename = f"{safe_title}_{safe_artist}".replace(" ", "_")
        
        pdf_filename = f"{base_filename}.pdf"
        docx_filename = f"{base_filename}.docx"
        
        pdf_bytes = generate_pdf_bytes(title, artist, key, lines)
        with open(pdf_filename, "wb") as f:
            f.write(pdf_bytes)
        print(f"PDF gerado com sucesso: {pdf_filename}")
        
        docx_bytes = generate_docx_bytes(title, artist, key, lines)
        with open(docx_filename, "wb") as f:
            f.write(docx_bytes)
        print(f"DOCX gerado com sucesso: {docx_filename}")
        
    except Exception as e:
        print(f"Erro: {e}")
