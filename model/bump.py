import requests

from config.config import BookConfig, BumpConfig


def do_bump(s: requests.Session, ids: list) -> None:
    s.headers.update({"Referer", BookConfig.PAGE_URL})
    try:
        response = s.post(BumpConfig.ACTION_URL, BumpConfig.request_template(ids))
    except requests.RequestException:
        print("Connectivity error for bump request.")
        return quit(0)

    if response.status_code != 304:
        print("Unable to bump book.")
        return quit(0)
