
import re
import time
from googlesearch import search

# --- Configuration ---
SOURCE_FILE = 'researchJumpOff.md'
OUTPUT_FILE = 'updated_research_links.md'
# Add more filetypes if needed, in order of preference
PREFERRED_FILETYPES = ['pdf', 'html', 'txt'] 

def extract_titles_from_markdown(filename):
    """Extracts titles from list items in the markdown file."""
    titles = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for lines starting with '* '
                if line.strip().startswith('* '):
                    # Clean up the line
                    clean_line = line.strip()[2:]
                    
                    # The title is usually before the first parenthesis
                    title = re.split(r'\(', clean_line)[0].strip()
                    
                    # Further clean up potential markdown/URL remnants
                    title = re.split(r'\[', title)[0].strip()
                    title = title.replace('“', '').replace('”', '').replace('—', '-')
                    
                    # Avoid adding empty or very short strings
                    if len(title) > 10: # Heuristic for a decent title length
                        titles.append(title)
    except FileNotFoundError:
        print(f"Error: Source file '{filename}' not found.")
    return sorted(list(set(titles)))

def find_best_url_for_title(title):
    """Searches Google for a title and returns the most promising URL."""
    print(f"Searching for: \"{title}\"")
    
    for filetype in PREFERRED_FILETYPES:
        try:
            query = f'\"{title}\" filetype:{filetype}'
            # search() returns a generator, get the first result
            search_results = search(query, num_results=1, sleep_interval=2)
            
            first_result = next(search_results, None)
            
            if first_result:
                print(f"  -> Found [{filetype.upper()}]: {first_result}")
                return first_result
                
        except Exception as e:
            # This can happen with HTTP 429: Too Many Requests
            print(f"  -> An error occurred during search: {e}")
            print("  -> Sleeping for 60 seconds to handle rate limiting...")
            time.sleep(60)
            # Retry the current search once
            try:
                search_results = search(query, num_results=1)
                first_result = next(search_results, None)
                if first_result:
                    print(f"  -> Found [{filetype.upper()}]: {first_result}")
                    return first_result
            except Exception as e2:
                print(f"  -> Retry failed: {e2}")

    print(f"  -> No direct file link found for \"{title}\".")
    return None


def main():
    """Main function to extract titles, search, and write the new file."""
    titles = extract_titles_from_markdown(SOURCE_FILE)
    
    if not titles:
        print("No titles were extracted. Exiting.")
        return

    print(f"Extracted {len(titles)} unique titles. Now searching for updated links...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Updated Research Links\n\n")
        f.write("> Automatically generated list of updated URLs based on title searches.\n\n---\n\n")
        
        for title in titles:
            best_url = find_best_url_for_title(title)
            
            if best_url:
                f.write(f"* {title}\n  * [Found Link]({best_url})\n\n")
            else:
                f.write(f"* {title}\n  * *No reliable link found.*\n\n")
            
            # Be a good web citizen, sleep between requests
            time.sleep(3) 

    print(f"\nProcess complete. See '{OUTPUT_FILE}' for the updated list of links.")


if __name__ == "__main__":
    main()
