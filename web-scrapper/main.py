import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_google_patents(query, max_results=10):
    """
    Searches Google Patents for a given query and returns the titles and links of the results.

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to fetch.

    Returns:
        list: A list of dictionaries containing titles and links of the patents.
    """
    base_url = "https://patents.google.com/"
    search_url = f"{base_url}?q={query.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # Extracting patent titles and links
    patents = soup.select(".result-title")
    for patent in patents[:max_results]:
        title = patent.text.strip()
        link = base_url + patent["href"].strip()
        results.append({"Title": title, "Link": link})

    return results

def save_to_csv(data, filename="patent_results.csv"):
    """
    Saves the patent data to a CSV file.

    Args:
        data (list): List of dictionaries containing patent titles and links.
        filename (str): The name of the output CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    query = input("Enter your patent search query: ")
    max_results = int(input("Enter the number of results to fetch: "))

    print("Searching Google Patents...")
    results = search_google_patents(query, max_results)

    if results:
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['Title']}")
            print(f"   Link: {result['Link']}")

        save_to_csv(results)
    else:
        print("No results found or an error occurred.")
