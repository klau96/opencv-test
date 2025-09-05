import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(dir)  # go up to project root directory
faces_folder = os.path.join(root, "faces")
raw_folder = os.path.join(root, "raw")

load_dotenv()
IMAGES_API_KEY = os.getenv("IMAGES_API_KEY")
IMAGES_CX = os.getenv("IMAGES_CX")

# -------- STARTOF configuration --------

base_url = "https://customsearch.googleapis.com/customsearch/v1"

default_headers = {
    "Accept": "application/json",
}

default_params = {
    "searchType": "image",
    "imgType": "face",
    "cx": f"{IMAGES_CX}",
    "key": f"{IMAGES_API_KEY}",
}

# -------- ENDOF configuration --------


def get_request(user_search_query, page_info):
    """
    Parameter: user_search_query

    Given the user's search query, send a request with the compiled headers / default parameters

    Return: requests.Models.Response
    """
    all_query_params = default_params.copy()
    all_query_params.update(user_search_query)
    all_query_params.update(page_info)

    request_object = requests.Request(
        method="GET", url=base_url, headers=default_headers, params=all_query_params
    )

    response = requests.get(request_object.url, request_object.params)
    response.raise_for_status()

    return response


image_extensions_dict = {
    "image/jpeg": "jpeg",
    "image/png": "png",
}


def check_image_extension(response):
    """
    Given a GET response, check "Content-Type" and verify with image extensions dictionary
    Return image's extension, if valid
    """
    content_type = response.headers.get("Content-Type")
    if content_type in image_extensions_dict:
        return image_extensions_dict[content_type]
    else:
        return False


def create_unique_path(query_filename, url, image_extension):
    print("create unique: ", query_filename)
    return query_filename + url[-10:] + "." + image_extension


def save_file_to_folder(response, query_filename, path):
    # TODO: Error handling for new file

    # Create new folder if not existing
    image_folder_dir = os.path.join(faces_folder, query_filename)
    filepath = os.path.join(image_folder_dir, path)

    try:
        os.makedirs(image_folder_dir, exist_ok=True)
    except OSError as e:
        print(f"🚨 Error making directory. ")
        exit(1)

    # Write file to custom made path
    with open(filepath, "wb") as file:
        file.write(response.content)
        file.close()


def download_from_url(url, query_filename):
    """
    Given a url, user query_filename (e.g. "markiplier_dog"), and path to folder,
    Download a file
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"🚨 ERROR: Request Exception when downloading — {url}")
        return None

    image_extension = check_image_extension(response)
    if image_extension:
        path = create_unique_path(query_filename, url, image_extension)
        query_filename
        save_file_to_folder(response, query_filename, path)
        return os.path.join(faces_folder, query_filename)
    else:
        print(
            f"🚨 ERROR CODE 415 — download_from_url(): Incorrect File Extension returned. {url}"
        )
    return response


def send_search(query, total_results_needed=10):
    user_search_query = {"q": query}
    current_start = 1
    num_per_page = default_params["num"]

    # TODO: Paginate results by implementing logic to control "start" and "num" request parameters

    response = get_request(user_search_query=user_search_query)
    print(
        "send_search RESPONSE:",
        response,
        response.headers.get("Content-Type", ""),
        type(response),
    )

    query_filename = query.replace(" ", "_").replace(",", "")

    data = response.json()

    with open(f"{os.path.join(raw_folder, query_filename)}.txt", "w") as file:
        # Error Handling: Items is missing or has none
        if not "items" in data or not len(data["items"]) > 0:
            print("\n🚨 ERROR: Items from response.json() invalid / incorrect length!")
            exit(1)

        # Loop through every item in the image search results
        for item in data["items"]:
            if "link" in item:
                link = item["link"]
                print(f"✅ Item Link: {item['link']}")
                download_from_url(url=link, query_filename=query_filename)
            else:
                print(f"🚧 CAUTION: Item {item} has no link to image!")

        json.dump(data, file)
        file.close()


people_list = [
    "markiplier",
    "jackscepticeye",
    "pewdiepie",
    "kim chaewon",
    "ali abdaal",
    "chloe shih",
]

# send_search(query="markiplier")

for person in people_list:
    print(f"======== STARTING SEARCH: {person} =========")
    send_search(person)
