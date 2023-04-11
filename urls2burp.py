import requests
import sys
import urllib3

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read the list of URLs from a file
if len(sys.argv) < 2:
    print("Usage: python urls2burp.py urls_file.txt")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        urls = [url.strip() for url in file.readlines()]
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)

# Burp Suite's proxy settings
proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

# Send requests to the URLs through Burp Suite's proxy
for url in urls:
    try:
        response = requests.get(url, proxies=proxy, timeout=10, verify=False)
        print(f"Request sent to {url}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {e}")

print("Finished sending requests.")
