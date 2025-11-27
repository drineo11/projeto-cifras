from lib.cifra_logic import get_cifra_content
import sys

url = "https://www.cifraclub.com.br/livres-para-adorar/liberdade/#google_vignette=true"

print(f"Testing URL: {url}")

try:
    title, artist, key, lines = get_cifra_content(url)
    print(f"Success!")
    print(f"Title: {title}")
    print(f"Artist: {artist}")
    print(f"Key: {key}")
    print(f"Number of lines: {len(lines)}")
    # Print first few lines to verify content
    for i in range(min(5, len(lines))):
        print(lines[i])
except Exception as e:
    print(f"Error: {e}")
