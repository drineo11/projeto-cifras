import sys
import os
sys.path.append(os.getcwd())
from lib.cifra_logic import get_cifra_content

url = "https://www.cifraclub.com.br/rachel-novaes/mil-motivos-para-agradecer/"
target_key = 0 # Should be A

print(f"Testing transposition for URL: {url} with key index {target_key}")
try:
    title, artist, key, lines = get_cifra_content(url, target_key)
    print(f"Title: {title}")
    print(f"Artist: {artist}")
    print(f"Key: {key}")
    
    print("-" * 20)
    
    target_key_2 = 3 # Should be C
    print(f"Testing transposition for URL: {url} with key index {target_key_2}")
    title, artist, key, lines = get_cifra_content(url, target_key_2)
    print(f"Title: {title}")
    print(f"Artist: {artist}")
    print(f"Key: {key}")
    print("-" * 20)
    print("First 10 lines of content:")
    for line in lines[:10]:
        text = ""
        for seg in line:
            text += seg['text']
        print(text)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
