import requests
import json

url = "http://127.0.0.1:5328/api/generate"
payload = {
    "url": "https://www.cifraclub.com.br/livres-para-adorar/liberdade/#google_vignette=true",
    "format": "pdf"
}
headers = {'Content-Type': 'application/json'}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    
    if response.status_code == 200:
        with open("test_api_output.pdf", "wb") as f:
            f.write(response.content)
        print("Saved test_api_output.pdf")
        print(f"Content Length: {len(response.content)}")
    else:
        print(f"Error Response: {response.text}")
except Exception as e:
    print(f"Request failed: {e}")
