from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.zippopotam.us"

printer = PrettyPrinter()

get_country = input("Enter the country code: ")
get_zip = input("Enter the zip code: ")
endpoint = f"/{get_country}/{get_zip}"

data = get(BASE_URL + endpoint).json()

def get_places():
    places = data["places"]
    return places

print(f"\nPlaces under the {get_zip} zip code:")
print(f"State: {get_places()[0]["state"]} ({get_places()[0]["state abbreviation"]})")

print("Places:")
for place in get_places():
    print(place["place name"])
