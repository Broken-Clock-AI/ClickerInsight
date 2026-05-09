import json
from datetime import datetime
from google_play_scraper import reviews, Sort

def scrape_app_reviews(app_id, lang='en', country='us', count=1000):
    """
    Scrapes a specified number of reviews for a given Google Play app ID.
    """
    print(f"Starting to scrape reviews for {app_id}...")
    
    # We use Sort.NEWEST to get the most recent feedback.
    result, continuation_token = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=count
    )

    # If the scraper returns fewer reviews than requested, it might be because there aren't enough.
    if not result:
        print("No reviews were returned. The app ID might be incorrect or there are no reviews.")
        return None

    print(f"Successfully scraped {len(result)} reviews.")
    return result

def json_converter(o):
    """
    Converts non-serializable objects for JSON, specifically datetime.
    """
    if isinstance(o, datetime):
        return o.__str__()

def save_reviews_to_json(reviews_data, app_id):
    """
    Saves the scraped review data to a JSON file.
    """
    if not reviews_data:
        print("No review data to save.")
        return

    output_path = f'market_analysis/scraped_data/{app_id}_reviews.json'
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(reviews_data, f, indent=2, ensure_ascii=False, default=json_converter)
        print(f"Successfully saved reviews to {output_path}")
    except IOError as e:
        print(f"Error: Could not write to file {output_path}. Error: {e}")

def main():
    """
    Main function to define app and orchestrate scraping and saving.
    """
    # App ID for "Egg, Inc."
    # URL: https://play.google.com/store/apps/details?id=com.auxbrain.egginc
    APP_ID = 'com.auxbrain.egginc'
    
    scraped_reviews = scrape_app_reviews(APP_ID)
    save_reviews_to_json(scraped_reviews, APP_ID)

if __name__ == '__main__':
    main()
