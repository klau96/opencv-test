import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
IMAGES_API_KEY = os.getenv("IMAGES_API_KEY")
IMAGES_CX = os.getenv("IMAGES_CX")
# functionality
#   download images from google search
#   given parameters: name, limit,

base_url = "https://cse.google.com/cse"
url_with_keys = f"{base_url}?cx={IMAGES_CX}?key={IMAGES_API_KEY}"

headers = {
    "Accept": "application/json",
    "searchType": "image",
    "num": 10,
    "imgType": "face",
}


def get_request(query_params):
    local_headers = headers.copy()
    local_headers.update(query_params)

    request_object = requests.Request(method="GET", url=base_url, headers=local_headers)
    result = requests.get(request_object.url, request_object.params)

    return result


def parse_GET_results():
    return requests.get("https://google.com")


search_markiplier = {
    "exactTerms": "markiplier",
}

result = get_request(query_params=search_markiplier)
print(result)

with open("markiplier.txt", "w") as file:

    file.write(str(result.json()))
