from antigate import AntiGate
import requests

API_KEY = "401446c86f02e43141a7333030229c4d"


def get_code(file_name: str) -> str:
    return str(AntiGate(API_KEY, file_name))


def download_photo(image_url, filename):
    img_data = requests.get(image_url).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)
