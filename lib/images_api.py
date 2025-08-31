import os
import dotenv
import axios

from dotenv import load_dotenv

load_dotenv()

IMAGES_API_KEY = os.getenv("IMAGES_API_KEY")

# functionality
#   download images from google search
#   given parameters: name, limit,

print(f"images api key: {IMAGES_API_KEY}")
