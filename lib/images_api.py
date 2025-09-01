import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
IMAGES_API_KEY = os.getenv("IMAGES_API_KEY")
IMAGES_CX = os.getenv("IMAGES_CX")

base_url = "https://customsearch.googleapis.com/customsearch/v1"

default_headers = {
    "Accept": "application/json",
}

default_params = {
    "num": "10",
    "searchType": "image",
    "imgType": "face",
    "cx": f"{IMAGES_CX}",
    "key": f"{IMAGES_API_KEY}",
}


def get_request(user_search_query):
    """
    Parameter: user_search_query

    Given the user's search query, send a request with the compiled headers / default parameters

    Return: requests.Models.Response
    """
    all_query_params = default_params.copy()
    all_query_params.update(user_search_query)

    request_object = requests.Request(
        method="GET", url=base_url, headers=default_headers, params=all_query_params
    )

    result = requests.get(request_object.url, request_object.params)
    result.raise_for_status()

    return result


search_markiplier = {
    "q": "markiplier",
}

result = get_request(user_search_query=search_markiplier)
print("RESULT:", result, result.headers.get("Content-Type", ""), type(result))

with open("markiplier.txt", "w") as file:
    data = result.json()
    # Error Handling: Items is missing or has none
    if not "items" in data or not len(data["items"]) > 0:
        print("\nERROR: Items from result.json() invalid / incorrect length!")
        exit(1)

    for item in data["items"]:
        if "link" in item:
            print(f"✅ Item Link: {item['link']}")
        else:
            print(f"🚧 CAUTION: Item {item} has no link to image!")
    file.close()
