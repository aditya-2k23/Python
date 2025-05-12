from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.zippopotam.us"

printer = PrettyPrinter()

get_country = input("Enter the country code: ")
get_zip = input("Enter the zip code: ")
endpoint = f"/{get_country}/{get_zip}"

try:
    response = get(BASE_URL + endpoint)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        def get_places():
            places = data["places"]
            return places

        print(f"\nPlaces under the {get_zip} zip code:")
        print(f"State: {get_places()[0]['state']} ({get_places()[0]['state abbreviation']})")

        print("Places:")
        for place in get_places():
            print(place["place name"])
    else:
        print(f"Error: The country code '{get_country}' or zip code '{get_zip}' does not exist in the database.")
        print(f"Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your internet connection or try a different country or zip code.")
