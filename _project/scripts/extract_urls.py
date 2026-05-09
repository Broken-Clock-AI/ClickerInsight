import re

def extract_urls(input_file, output_file):
    """
    Extracts all unique URLs from a markdown file and saves them to a text file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find all URLs in markdown format [text](url)
    urls = re.findall(r'\((https?://.*?)\)', content)
    
    # Get unique URLs and sort them
    unique_urls = sorted(list(set(urls)))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for url in unique_urls:
            f.write(url + '\n')

if __name__ == '__main__':
    extract_urls('talkResearch.md', 'urls.txt')