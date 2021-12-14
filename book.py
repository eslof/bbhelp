import urllib.parse
import requests

from config import BookConfig


def get_oldest(
    s: requests.Session, request_number: int, book_count: int, timestamp: int
) -> dict:
    s.headers.update({"Referer", BookConfig.PAGE_URL})
    request_url = BookConfig.JSON_URL + urllib.parse.urlencode(
        BookConfig.request_template(request_number, book_count, timestamp)
    )

    try:
        response = s.get(request_url)
    except requests.RequestException:
        print("Connectivity error for oldest books.")
        return quit(0)

    if response.status_code != 304:
        print("Unable to retrieve oldest books.")
        return quit(0)

    try:
        json_data = response.json()
    except (ValueError, IndexError, KeyError):
        print("JSON parsing/format error for oldest books.")
        return quit(0)

    if "data" not in json_data or len(json_data["data"]) == 0:
        print("No data found in oldest books request.")
        return quit(0)

    return json_data["data"]
