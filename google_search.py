import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env file

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")


def search_recipes(ingredients, num_results=5):
    if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
        print("❌ API key not found. Please set up .env file.")
        return []

    query = " ".join(ingredients) + " recipe"

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "num": num_results
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    return response.json().get("items", [])
