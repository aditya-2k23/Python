from crawlbase import CrawlingAPI
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
CRAWLBASE_API_KEY = os.getenv("CRAWLBASE_API_KEY")

crawling_api = CrawlingAPI({'token': CRAWLBASE_API_KEY})

def scrape_google_results(query, page):
    url = f"https://www.google.com/search?q={query}&start={page * 10}"
    options = {'scraper': 'google-serp'}
    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        response_data = json.loads(response['body'].decode('latin1'))
        return response_data.get('body', {})
    else:
        print("Failed to fetch data.")
        return {}

def scrape_all_pages(query, max_pages):
    all_results = []
    for page in range(max_pages):
        print(f"Scraping page {page + 1}...")
        page_results = scrape_google_results(query, page)
        if not page_results:  # Stop if no more results are found
            print("No more results, stopping.")
            break
        all_results.append(page_results)
    return all_results

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    print("Enter your search query:")
    query = input()
    max_pages = 2
    results = scrape_all_pages(query, max_pages)
    save_to_json(results, "./web-scrapper/google_search_results.json")
