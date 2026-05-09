"""
SCRIPT: convert_to_markdown.py
ROLE: Ingestion Utility (v1.0 Legacy)
STATUS: STABLE UTILITY

DESCRIPTION:
    Converts HTML downloads into clean Markdown for extraction.

HFS v2.1 NOTE:
    This tool remains valid for the 'Markdown Normalization' step of Phase 1.
"""

import os
import re
try:
    import html2text
except ImportError:
    print("The 'html2text' library is not installed. Please install it using 'pip install html2text'")
    exit()

def convert_html_to_markdown(input_dir, output_dir):
    """
    Converts all HTML files in the input_dir to Markdown and saves them to the output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for filename in os.listdir(input_dir):
        if filename.endswith(".html"):
            html_filepath = os.path.join(input_dir, filename)
            markdown_filename = os.path.splitext(filename)[0] + ".md"
            markdown_filepath = os.path.join(output_dir, markdown_filename)
            
            try:
                with open(html_filepath, 'r', encoding='utf-8') as f:
                    html_content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(html_filepath, 'r', encoding='latin-1') as f:
                        html_content = f.read()
                except Exception as e:
                    print(f"Error reading {filename} with different encodings: {e}")
                    continue
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                continue

            try:
                h = html2text.HTML2Text()
                h.ignore_links = True
                markdown_content = h.handle(html_content)
                
                with open(markdown_filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                print(f"Converted {html_filepath} to {markdown_filepath}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == '__main__':
    convert_html_to_markdown('research_assets/downloads/from_talkResearch', 'research_assets/markdown_conversions/from_talkResearch')