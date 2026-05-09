"""
Python script to automatically search storefront URLs for a list of game titles.

Requires:
  - GOOGLE_API_KEY (Google Custom Search API)
  - GOOGLE_CSE_ID  (Custom Search Engine ID)

Reads game titles from:
  - ../market_analysis/game_titles.md

Output:
  - ../storefront_results.csv (relative to the script's location)
"""

import os
import csv
import time
import requests

# --- Configuration ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GAME_LIST_PATH = os.path.join(os.path.dirname(__file__), '..', 'market_analysis', 'game_titles.md')
OUTPUT_CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'storefront_results.csv')

def get_game_titles(file_path):
    """Reads the master list of games from the markdown file."""
    if not os.path.exists(file_path):
        print(f"❌ ERROR: Game list not found at {file_path}")
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    game_titles = []
    for line in lines:
        if line.strip().startswith('- '):
            # Remove the '- ' and any leading/trailing whitespace
            title = line.strip()[2:].strip()
            game_titles.append(title)
            
    print(f"✅ Found {len(game_titles)} games in the list.")
    return game_titles

def search_game(game_title):
    """Searches Google for storefronts for a single game title."""
    query = f"{game_title} game Steam itch.io official site download"
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q={query}"

    try:
        res = requests.get(url)
        res.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        data = res.json()

        results = []
        if "items" in data:
            for item in data["items"]:
                results.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                })
        return {"game": game_title, "results": results}
    except requests.exceptions.RequestException as err:
        return {"game": game_title, "error": str(err)}
    except Exception as err:
        return {"game": game_title, "error": f"An unexpected error occurred: {err}"}

def run():
    """Fetches all results and writes them to a CSV file."""
    if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
        print("❌ ERROR: Set your GOOGLE_API_KEY and GOOGLE_CSE_ID environment variables.")
        return

    games = get_game_titles(GAME_LIST_PATH)
    if games is None:
        return

    print(f"\n🔎 Running storefront discovery for {len(games)} games...\n")

    with open(OUTPUT_CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Game", "Result #", "Title", "URL", "Snippet"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for game in games:
            print(f"➡ Searching: {game}")
            output = search_game(game)

            if "error" in output and output["error"]:
                writer.writerow({
                    "Game": game,
                    "Result #": "",
                    "Title": "ERROR",
                    "URL": output["error"],
                    "Snippet": ""
                })
                continue

            for i, r in enumerate(output.get("results", [])):
                writer.writerow({
                    "Game": game,
                    "Result #": i + 1,
                    "Title": r["title"],
                    "URL": r["link"],
                    "Snippet": r["snippet"]
                })
            
            time.sleep(0.25)  # Small delay to avoid rate limiting

    print(f"\n✅ Done! Results written to {OUTPUT_CSV_PATH}")

if __name__ == "__main__":
    run()
