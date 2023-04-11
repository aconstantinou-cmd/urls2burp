# Burpsuite URL Importer

This Python script imports a list of URLs into Burpsuite's sitemap by sending requests to the URLs through Burpsuite's proxy.

## Requirements

- Python 3
- `requests` library

## Installation

1. Install the `requests` library if you haven't already:

```bash
pip install requests
```

# Usage
Create a text file with a list of URLs you want to import into Burpsuite's sitemap. Each URL should be on a separate line.

The script will send requests to the URLs through Burpsuite's proxy, which should be running on http://127.0.0.1:8080. The URLs will be automatically added to Burpsuite's sitemap.
# Troubleshooting

Ensure that Burpsuite is running, and its proxy is set up on http://127.0.0.1:8080.
Check that the URLs in your list are valid and reachable.
Check if the sitemap has any filters that prevent the urls from appearing. I normally check show all.

Make sure the requests library is installed, and the script is using Python 3.
