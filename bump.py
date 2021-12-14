import requests

from config import BookConfig, BumpConfig


def do_bump(s: requests.Session, ids: list) -> None:
    s.headers.update({"Referer", BookConfig.PAGE_URL})
    try:
        response = s.post(BumpConfig.ACTION_URL, get_bump_request(ids))
    except requests.RequestException:
        print("Connectivity error for bump request.")
        return quit(0)

    if response.status_code != 304:
        print("Unable to bump book.")
        return quit(0)


def get_bump_request(ids: list) -> dict:
    return {
        "manage_product_ids": ",".join(ids),
        "product_action[]": "bump",
        "inc": "",
        "dec": "",
    }
