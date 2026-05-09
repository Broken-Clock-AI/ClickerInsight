
import re
import os
from urllib.parse import urlparse, unquote

# --- Configuration ---
MARKDOWN_FILE = 'researchJumpOff.md'
DOWNLOADS_DIR = 'downloads'
OUTPUT_FILE = 'non_retrieved_resources.md'

def get_all_original_urls(filename):
    """Extracts all unique http/https URLs from the source markdown file."""
    urls = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            # Corrected regex: escapes the brackets and handles markdown parenthesis
            url_pattern = r'https?://[^\s()]+'
            urls = sorted(list(set(re.findall(url_pattern, content))))
    except FileNotFoundError:
        print(f"Error: Source file '{filename}' not found.")
    return urls

def map_urls_to_titles(filename):
    """Creates a dictionary mapping URLs to their titles from the markdown file."""
    url_title_map = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        current_title = ""
        for line in lines:
            # Look for titles in list items
            if line.strip().startswith('*'):
                cleaned_title = re.split(r'\(|\[' , line.strip())[0].replace('*', '').strip()
                if len(cleaned_title) > 10 and "http" not in cleaned_title:
                    current_title = cleaned_title
            
            # Find URLs in the line
            url_pattern = r'https?://[^\s()]+'
            found_urls = re.findall(url_pattern, line)
            
            if found_urls and current_title:
                for url in found_urls:
                    # Clean trailing characters that might be caught by regex
                    url = url.rstrip(')') 
                    if url not in url_title_map:
                        url_title_map[url] = current_title
                        
    except FileNotFoundError:
        print(f"Error: Markdown file '{filename}' not found.")
        
    return url_title_map

def check_if_retrieved(url, downloaded_files):
    """Checks if a URL appears to have been downloaded based on sanitized filenames."""
    # This is a best-effort check. A perfect mapping is difficult.
    try:
        parsed = urlparse(unquote(url))
        domain = parsed.netloc.replace('www.', '')
        
        # Create a simplified signature from the URL to check against filenames
        # Use parts of the path and query, alphanumeric only
        path_parts = [part for part in parsed.path.split('/') if part]
        path_signature = ''.join(path_parts)[:50]
        
        for filename in downloaded_files:
            if domain in filename:
                # If domain matches, check if a significant part of the path also matches
                if path_signature in re.sub(r'[^a-zA-Z0-9]', '', filename):
                    return True
    except Exception:
        # Ignore parsing errors for malformed URLs
        return False
    return False

def main():
    original_urls = get_all_original_urls(MARKDOWN_FILE)
    url_to_title_map = map_urls_to_titles(MARKDOWN_FILE)
    
    try:
        downloaded_files = os.listdir(DOWNLOADS_DIR)
    except FileNotFoundError:
        print(f"Error: Downloads directory '{DOWNLOADS_DIR}' not found.")
        downloaded_files = []

    non_retrieved = {} # Using a dict to store title -> url to avoid duplicate titles
    for url in original_urls:
        if not check_if_retrieved(url, downloaded_files):
            title = url_to_title_map.get(url, "Unknown Title - Check Manually")
            # For duplicate URLs pointing to the same title, we only add it once
            if title not in non_retrieved:
                 non_retrieved[title] = url

    if not non_retrieved:
        print("All resources appear to have been successfully downloaded.")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Non-Retrieved Resources\n\n")
        f.write("> A list of resources from the original bibliography that could not be automatically downloaded.\n\n---\n\n")
        
        # Use the url_to_title_map to preserve order somewhat and filter
        final_list = {}
        for url, title in url_to_title_map.items():
            if url in non_retrieved.values():
                 # A final filter for relevance
                if 'game' in title.lower() or 'play' in title.lower() or 'clicker' in title.lower():
                    final_list[title] = url
        
        for title, url in sorted(final_list.items()):
            f.write(f"* **{title}**\n  * Original Link: `{url}`\n\n")
    
    print(f"Generated a list of {len(final_list)} non-retrieved resources in '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
