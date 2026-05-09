# Project Manifest

This document provides a comprehensive overview of the `clickerResearch` project, detailing its components, data flow, and purpose. It was generated to deconstruct and analyze the project's structure.

---

## 1. Scripts (`/scripts`)

This directory contains all automation, scraping, and analysis scripts.

| Script | Language | Purpose | Inputs | Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **`analyze_sentiment.py`** | Python | Analyzes scraped game reviews for sentiment, identifies key positive/negative themes, and generates a summary report. | `market_analysis/scraped_data/{app_id}_reviews.json` | `market_analysis/reports/{app_id}_sentiment_report.md` |
| **`concept_finder.py`** | Python | Reads the main tome, uses TF-IDF to extract and rank key concepts/phrases, and suggests them for the knowledge graph. | `tome/Tome.md` | Console output (list of concepts) |
| **`convert_to_markdown.py`** | Python | Converts downloaded HTML research articles into a clean Markdown format for easier analysis. | HTML files in `research_assets/downloads/from_talkResearch` | Markdown files in `research_assets/markdown_conversions/from_talkResearch` |
| **`extract_failed_titles.py`**| Python | Parses the download report, finds failed URLs, and cross-references them to identify the titles of missed articles. | `download_report.md`, `researchJumpOff.md` | Console output (list of titles) |
| **`extract_urls.py`** | Python | A simple utility to extract all unique URLs from a markdown file. | `talkResearch.md` | `urls.txt` |
| **`fetch_articles.py`** | Python | Fetches HTML content for a given list of URLs. Primarily used to re-attempt failed downloads. | `failed_urls.txt` | HTML files in `research_assets/downloads/from_talkResearch` |
| **`fetch_research.py`** | Python | The primary download script. Reads URLs, downloads various file types (PDF, HTML), and generates a detailed report. | `updated_links.md` | Files in `/downloads`, `download_report.md` |
| **`find_storefronts.py`** | Python | Reads the master game list and uses the Google Search API to find storefront URLs (Steam, itch.io, etc.). | `market_analysis/game_titles.md` | `storefront_results.csv` |
| **`find_updated_links.py`** | Python | Extracts titles from the bibliography, searches Google to find fresh, direct download links, and creates a new list. | `researchJumpOff.md` | `updated_research_links.md` |
| **`generate_missing_list.py`**| Python | Audits the `downloads` folder against the original URL list and reports which resources were not successfully retrieved. | `researchJumpOff.md`, `/downloads` folder | `non_retrieved_resources.md` |
| **`knowledge_builder.py`** | Python | Core synthesis script. Builds a knowledge graph by linking tome chapters, research papers, and key concepts. | Files in `/tome` and `/research_assets/markdown_conversions` | `app/knowledge_graph.json` |
| **`rank_games.py`** | Python | Counts the mentions of game titles within a body of text and outputs the frequency in JSON format. | `<game_titles_file>`, `<content_file>` | Console output (JSON data) |
| **`scrape_reviews.py`** | Python | Scrapes Google Play Store reviews for a specific app ID. | `google_play_scraper` library | `market_analysis/scraped_data/{app_id}_reviews.json` |
| **`scrape_steam_reviews.py`**| Python | Scrapes Steam store reviews for a specific app ID. | `steamreviews` library | `market_analysis/scraped_data/steam_{app_id}_reviews.json` |
| **`scrape_steam_page.ps1`** | PowerShell | Creates a complete, self-contained offline snapshot of a single web page, including all local assets. | URL, Output Directory | A folder containing the full web page |

---

## 2. Data & Research Flow

This section outlines the directories and the typical flow of data from raw input to synthesized output.

### Phase 1: Market & Topic Intelligence (Data Gathering)

1.  **Source Identification:**
    *   `talkResearch.md`: Contains initial brainstorming and links.
    *   `market_analysis/best_of_lists.md`: A curated list of articles/videos recommending games.

2.  **URL Extraction & Game List Generation:**
    *   `extract_urls.py` processes `talkResearch.md` to produce `urls.txt`.
    *   *Manual process:* The links in `best_of_lists.md` are analyzed to produce `market_analysis/game_titles.md` (the master list) and `market_analysis/game_rankings.md` (based on mention frequency).

3.  **Storefront Discovery:**
    *   `find_storefronts.py` takes the master game list and searches for where to find/buy them, producing `storefront_results.csv`.

4.  **Review Scraping & Analysis:**
    *   `scrape_reviews.py` and `scrape_steam_reviews.py` download reviews for specific, high-interest games (e.g., *Egg Inc.*, *Cookie Clicker*), saving them as JSON files in `market_analysis/scraped_data/`.
    *   `analyze_sentiment.py` processes these JSON files to create human-readable reports in `market_analysis/reports/`.

### Phase 2: Academic & Article Corpus (Literature Review)

1.  **Initial Bibliography:**
    *   `researchJumpOff.md`: The starting list of academic papers and relevant articles.

2.  **Link Verification & Downloading:**
    *   `find_updated_links.py` attempts to find fresh URLs for the titles in the bibliography, creating `updated_research_links.md`.
    *   `fetch_research.py` takes this updated list and systematically downloads the resources into the `/downloads` directory, creating `download_report.md`.

3.  **Error Handling & Conversion:**
    *   `generate_missing_list.py` and `extract_failed_titles.py` are used to audit the downloads and identify what failed. `failed_urls.txt` can be used with `fetch_articles.py` for retry attempts.
    *   `convert_to_markdown.py` processes the downloaded HTML files into clean `.md` files in `research_assets/markdown_conversions/` for analysis.

### Phase 3: Synthesis & Application

1.  **The Tome:**
    *   The `/tome` and `/new_tome` directories contain the final written output, structured into chapters. This is the culmination of the research.

2.  **Knowledge Graph Generation:**
    *   `knowledge_builder.py` reads all the Markdown files in `/tome` and `/research_assets/markdown_conversions/`.
    *   It generates `app/knowledge_graph.json`, which connects concepts, research papers, and tome chapters based on citations and keyword mentions.

3.  **Web Application:**
    *   The `/app` directory contains a simple front-end (HTML, CSS, JS) that visualizes the `knowledge_graph.json`, allowing for interactive exploration of the research.
