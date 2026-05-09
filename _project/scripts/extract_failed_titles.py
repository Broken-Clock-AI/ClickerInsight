
import re

def get_failed_urls(report_file):
    """Parses the download report and returns a list of failed URLs."""
    failed_urls = []
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            # Check if the line indicates a failure
            if '❌ Failed' in line or '❌ Error' in line:
                # The URL is typically in the line preceding the failure message
                if i > 0:
                    prev_line = lines[i-1]
                    # Extract URL from markdown link format '* **...**'
                    match = re.search(r'\* \*\*https?://[^\s\*]+\*\*?', prev_line)
                    if match:
                        # Clean up the matched string to get a raw URL
                        url = match.group(0).replace('*', '').strip()
                        if url not in failed_urls:
                            failed_urls.append(url)
    except FileNotFoundError:
        print(f"Error: Report file '{report_file}' not found.")
    return failed_urls


def map_urls_to_titles(markdown_file, urls_to_find):
    """Finds the titles corresponding to a list of URLs from the markdown file."""
    url_title_map = {}
    url_set = set(urls_to_find)
    
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            for url in url_set:
                if url in line:
                    # Title is likely the list item on the line above the URL
                    # or a few lines above. We search backwards.
                    for j in range(i - 1, max(-1, i - 4), -1):
                        prev_line = lines[j]
                        if prev_line.strip().startswith('*'):
                            # Clean up the title
                            title = re.split(r'\(|\[' , prev_line.strip())[0].replace('*', '').strip()
                            # Filter out non-title lines
                            if len(title) > 10 and "http" not in title:
                                url_title_map[url] = title
                                break # Found title for this URL
                    break # Found URL, move to next line
    except FileNotFoundError:
        print(f"Error: Markdown file '{markdown_file}' not found.")
        
    return url_title_map

def main():
    report_file = 'download_report.md'
    markdown_file = 'researchJumpOff.md'
    
    failed_urls = get_failed_urls(report_file)
    if not failed_urls:
        print("No failed URLs found in the report.")
        return
        
    title_map = map_urls_to_titles(markdown_file, failed_urls)
    
    if not title_map:
        print("Could not map any failed URLs to titles.")
        return

    # Print a clean list of titles for the next step
    for url, title in title_map.items():
        print(title)

if __name__ == "__main__":
    main()
