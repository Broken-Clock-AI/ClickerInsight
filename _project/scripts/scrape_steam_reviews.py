import json
import steamreviews

def scrape_steam_reviews(app_id, lang='english', count=1000):
    """
    Scrapes a specified number of reviews for a given Steam app ID.
    """
    print(f"Starting to scrape Steam reviews for app ID {app_id}...")
    
    # The library fetches reviews in batches. We specify the total number we want.
    # review_dict contains 'reviews' and 'query_summary'
    review_dict, err = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params={'language': lang, 'num_per_page': 100})
    
    if err:
        print(f"Error fetching reviews: {err}")
        return None

    # We need to process the reviews from the dictionary structure
    reviews_list = review_dict.get('reviews', [])
    
    # The library might return more than the count, so we'll slice it if needed.
    # Note: The library aims to get a certain number but doesn't guarantee an exact count.
    reviews_to_save = list(reviews_list.values())[:count]

    if not reviews_to_save:
        print("No reviews were returned. The app ID might be incorrect or there are no reviews.")
        return None

    print(f"Successfully scraped {len(reviews_to_save)} reviews.")
    return reviews_to_save

def save_reviews_to_json(reviews_data, app_id_str):
    """
    Saves the scraped review data to a JSON file.
    The datetime objects from the API are Unix timestamps, which are JSON-serializable numbers.
    """
    if not reviews_data:
        print("No review data to save.")
        return

    output_path = f'market_analysis/scraped_data/steam_{app_id_str}_reviews.json'
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(reviews_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved reviews to {output_path}")
    except IOError as e:
        print(f"Error: Could not write to file {output_path}. Error: {e}")

def main():
    """
    Main function to define app and orchestrate scraping and saving.
    """
    # App ID for "Cookie Clicker" on Steam
    # Found in the URL: https://store.steampowered.com/app/1454400/Cookie_Clicker/
    APP_ID = 1454400
    
    scraped_reviews = scrape_steam_reviews(APP_ID)
    save_reviews_to_json(scraped_reviews, str(APP_ID))

if __name__ == '__main__':
    main()
