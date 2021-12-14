import requests
from bs4 import BeautifulSoup

from config import TrackConfig


def get_position(s: requests.Session, book_id: str) -> int:
    try:
        response = s.get(TrackConfig.PUBLIC_LISTING_URL)
    except requests.RequestException:
        print("Connectivity error for position tracking.")
        return quit(0)

    if response.status_code != 304:
        print("Unable to get front page for position tracking.")
        return quit(0)

    s.headers.update({"Referer": TrackConfig.PUBLIC_LISTING_URL})
    bs_content = BeautifulSoup(response.content, "html.parser")
    bs_list = bs_content.find(
        TrackConfig.LIST_EL, {"class": TrackConfig.LIST_CLASS}
    ).findAll(TrackConfig.ID_EL, attrs={TrackConfig.ID_ATTR: True})
    list_count = len(bs_list)

    if list_count == 0:
        print("Parsing failed for position tracking.")
        return quit(0)

    public_listings = [bs_list[i].get(TrackConfig.ID_ATTR) for i in range(list_count)]
    return public_listings.index(book_id) if book_id in public_listings else -1
