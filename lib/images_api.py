import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
IMAGES_API_KEY = os.getenv("IMAGES_API_KEY")
IMAGES_CX = os.getenv("IMAGES_CX")

# -------- STARTOF configuration --------

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

# -------- ENDOF configuration --------


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


def download_from_url(url, query, path):
    """
    Given a url, user query (e.g. "markiplier"), and path to folder,
    Download a file

    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"🚨 ERROR: Request Exception when downloading — {url}")

    # print(f"DOWNLOAD LINK for {path}: {response.content}")


def create_path_for_query_filename(query_filename):
    query_filename += ".jpg"
    return os.path.join(dir, "faces", query_filename)


def send_search(query):
    user_search_query = {"q": query}
    result = get_request(user_search_query=user_search_query)
    print("RESULT:", result, result.headers.get("Content-Type", ""), type(result))

    query_filename = query.replace(" ", "_")

    data = result.json()

    with open(f"{query_filename}.txt", "w") as file:

        # Error Handling: Items is missing or has none
        if not "items" in data or not len(data["items"]) > 0:
            print("\n🚨 ERROR: Items from result.json() invalid / incorrect length!")
            exit(1)

        # Loop through every item in the image search results
        for item in data["items"]:
            if "link" in item:
                link = item["link"]
                path = create_path_for_query_filename(query_filename)
                print(f"✅ Item Link: {item['link']}")
                download_from_url(url=link, query=query, path=path)
            else:
                print(f"🚧 CAUTION: Item {item} has no link to image!")

        file.close()


send_search(query="markiplier")
