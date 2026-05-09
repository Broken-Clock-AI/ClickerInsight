import urllib.request
import os
import re

def generate_filename_from_url(url):
    """
    Generates a valid filename from a URL.
    """
    # Remove http/https and www
    url = re.sub(r'https?://(www\.)?', '', url)
    # Replace special characters with underscores
    filename = re.sub(r'[^a-zA-Z0-9]', '_', url)
    # Add .html extension
    return filename + '.html'

def fetch_articles(url_file, output_dir):
    """
    Fetches the content of each URL in the url_file and saves it to the output_dir.
    """
    with open(url_file, 'r', encoding='utf-8') as f:
        urls = f.read().splitlines()
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    for url in urls:
        try:
            print(f"Fetching {url}...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                content = response.read()
            
            filename = generate_filename_from_url(url)
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(content)
            
            print(f"Saved to {filepath}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")

if __name__ == '__main__':
    fetch_articles('failed_urls.txt', 'research_assets/downloads/from_talkResearch')