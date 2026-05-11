# scripts/

This directory contains Python and PowerShell scripts used for research automation, data scraping, and systemic analysis.

## Key Scripts

### Research & Data Gathering
- **`fetch_research.py`**: Downloads academic papers and articles from a provided list of URLs.
- **`scrape_reviews.py` / `scrape_steam_reviews.py`**: Gathers player feedback for sentiment analysis.
- **`find_storefronts.py`**: Uses Google Search API to find store links for game titles.
- **`scrape_steam_page.ps1`**: Creates offline snapshots of Steam store pages.

### Analysis & Synthesis
- **`analyze_tome.py`**: Performs textual analysis on the research tome.
- **`knowledge_builder.py`**: Links tome chapters to research papers and concepts via citations.
- **`synthesis_analysis.py`**: Audits the synthesis quality and coverage.
- **`rank_games.py`**: Measures the frequency of game mentions across the corpus.

### Utility & Management
- **`convert_to_markdown.py`**: Sanitizes HTML downloads into clean Markdown for indexing.
- **`extract_urls.py`**: Gathers all unique URLs from project notes.
- **`find_updated_links.py`**: Finds fresh download mirrors for older academic papers.

---

*Note: Some scripts require API keys (e.g., Google Search API) stored in `.env`. These are ignored by source control.*
