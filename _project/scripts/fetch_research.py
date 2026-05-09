
import re
import os
import requests
from urllib.parse import urlparse, unquote
import datetime

# --- Configuration ---
SOURCE_FILE = 'updated_links.md'
DOWNLOAD_DIR = 'downloads'
REPORT_FILE = 'download_report.md'
USER_AGENT = 'Gemini-CLI-Research-Bot/1.0'
TIMEOUT_SECONDS = 20  # Max time to wait for a server response

# --- Main Script ---

def sanitize_filename(url):
    """Creates a filesystem-safe filename from a URL."""
    parsed = urlparse(unquote(url))
    path_parts = [part for part in parsed.path.split('/') if part]
    
    # Start with the domain
    filename = parsed.netloc.replace('www.', '')
    
    # Add path components, avoiding generic names
    if path_parts:
        last_part = path_parts[-1]
        if last_part.lower() not in ('', 'index.html', 'index.php', 'view'):
             # Try to get a meaningful name from the path
             filename += '_' + re.sub(r'[^a-zA-Z0-9_.-]', '', last_part)
        elif len(path_parts) > 1:
            # Fallback to the second to last part
             filename += '_' + re.sub(r'[^a-zA-Z0-9_.-]', '', path_parts[-2])

    # Handle query parameters for dynamic pages
    if parsed.query:
        filename += '_' + re.sub(r'[^a-zA-Z0-9_.-]', '', parsed.query)[:50]

    # Limit length
    return filename[:150]

def get_file_extension(response, url):
    """Determines a file extension from Content-Type or URL."""
    content_type = response.headers.get('Content-Type', '').lower()
    
    if 'application/pdf' in content_type:
        return '.pdf'
    if 'text/html' in content_type:
        return '.html'
    if 'text/plain' in content_type:
        return '.txt'
    if 'application/xml' in content_type or 'text/xml' in content_type:
        return '.xml'
    
    # Fallback to URL extension
    path = urlparse(url).path
    if '.' in path:
        ext = '.' + path.split('.')[-1]
        if len(ext) < 6: # a reasonable check for a file extension
            return ext
            
    return '.html' # Default for web content

def fetch_resources():
    """Main function to parse URLs, download, and report."""
    
    # --- 1. Read and Parse URLs ---
    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find the source file '{SOURCE_FILE}'.")
        return

    # Regex to find all http/https URLs in markdown links or just bare
    url_pattern = r'https?://[^\s\)">]+'
    urls = sorted(list(set(re.findall(url_pattern, content))))
    
    if not urls:
        print("No URLs found in the source file.")
        return

    print(f"Found {len(urls)} unique URLs. Starting download process...")
    
    # --- 2. Setup and Download ---
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    report_lines = []
    
    headers = {'User-Agent': USER_AGENT}
    
    with requests.Session() as session:
        session.headers.update(headers)
        
        for i, url in enumerate(urls):
            status = ''
            full_message = f"[{i+1}/{len(urls)}] Attempting: {url[:90]}..."
            print(full_message, end=' ') # Print without newline to allow status on same line
            
            try:
                # Use stream=True to avoid loading large files into memory at once
                with session.get(url, timeout=TIMEOUT_SECONDS, stream=True, allow_redirects=True) as response:
                    # After redirects, the final URL might have changed
                    final_url = response.url
                    
                    if response.status_code == 200:
                        ext = get_file_extension(response, final_url)
                        filename = sanitize_filename(final_url) + ext
                        filepath = os.path.join(DOWNLOAD_DIR, filename)
                        
                        # Save the content chunk by chunk
                        with open(filepath, 'wb') as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                f.write(chunk)
                                
                        status = f"✅ Success | 200 OK | Saved as `{filename}`"
                    else:
                        status = f"❌ Failed | HTTP {response.status_code} | {response.reason}"
            
            except requests.exceptions.RequestException as e:
                error_name = type(e).__name__
                status = f"❌ Error | {error_name} | Could not connect or timed out."
            
            print(status) # Print status with a newline
            report_lines.append(f"* **{url}**\n  * {status}\n")

    # --- 3. Write Report ---
    report_header = f"""# Download Report

*   **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
*   **Source File:** `{SOURCE_FILE}`
*   **Total URLs:** {len(urls)}
*   **Success Rate:** {len([line for line in report_lines if 'Success' in line])}/{len(urls)}

---
"""
    
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_header + "\n".join(report_lines))

    print(f"\nProcess complete. See '{REPORT_FILE}' for detailed results.")
    print(f"Downloaded files are in the '{DOWNLOAD_DIR}' directory.")


if __name__ == "__main__":
    fetch_resources()
