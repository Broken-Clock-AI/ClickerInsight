"""
SCRIPT: harvest_2026.py
ROLE: Automated Retrieval (DEPRECATED)
STATUS: ARCHIVED / DO NOT USE

DESCRIPTION:
    Legacy script used for harvesting 2026 papers. 

REASON FOR DEPRECATION:
    Contains hardcoded queries for hallucinated/fictional papers discovered during 
    the Reality Audit (May 8, 2026). Use the 'External Search Brief' for new searches.
"""

import os
import time
from googlesearch import search
import requests

# --- Configuration ---
SEARCH_QUERIES = [
    "\"The Ontology of Incremental Games: Thinking Like the Computer\" 2026",
    "\"Cozy Ecogames: Comfort, Relaxation, and the Ethics of Waiting\" 2026",
    "\"Idle Games: Engagement and Gameplay Patterns\" thesis 2025",
    "\"Agentic AI\" in idle game design 2026",
    "\"Machinic Thinking\" game research 2026"
]

OUTPUT_DIR = "0_research/research_assets/downloads/2026_harvest"
LOG_FILE = "1_synthesis/analysis/2026_harvest_log.md"

def setup_environment():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("# 2026 Research Harvesting Log\n\n")

def log_harvest(query, title, url, status):
    with open(LOG_FILE, 'a') as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"| {timestamp} | {query[:30]}... | [{title}]({url}) | {status} |\n")

def harvest():
    print(f"Starting 2026 Research Harvest...")
    setup_environment()
    
    for query in SEARCH_QUERIES:
        print(f"Searching: {query}")
        try:
            # Search for PDF specifically
            results = search(f"{query} filetype:pdf", num_results=3, sleep_interval=5)
            
            for url in results:
                filename = url.split("/")[-1]
                if not filename.endswith(".pdf"):
                    filename += ".pdf"
                
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                print(f"  Attempting download: {url}")
                try:
                    response = requests.get(url, timeout=15)
                    if response.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(response.content)
                        log_harvest(query, filename, url, "Success")
                        print(f"    Saved to {filepath}")
                        break # Only need one good version per query
                    else:
                        log_harvest(query, filename, url, f"Failed (HTTP {response.status_code})")
                except Exception as e:
                    log_harvest(query, filename, url, f"Error: {str(e)}")
            
            time.sleep(10) # Respectful delay
            
        except Exception as e:
            print(f"Search error for {query}: {e}")

if __name__ == "__main__":
    # Note: Requires 'googlesearch-python' and 'requests' libraries
    harvest()
