import requests

from bs4 import BeautifulSoup
from config.config import LoginConfig


def do_login(s: requests.session) -> None:
    if "Referer" in s.headers:
        del s.headers["Referer"]

    try:
        get_response = s.get(LoginConfig.PAGE_URL)
    except requests.RequestException:
        print("Connectivity error for login.")
        return quit(0)

    if get_response.status_code not in [200, 304]:
        print("Unable to get login page.")
        return quit(0)

    s.headers.update({"Referer": LoginConfig.PAGE_URL})
    bs_content = BeautifulSoup(get_response.content, "html.parser")
    token = bs_content.find(LoginConfig.FORM_NAME, {"name": LoginConfig.TOKEN_NAME})[
        "value"
    ]
    if not token:
        print("Parsing failed for login page.")

    try:
        post_response = s.post(LoginConfig.PAGE_URL, get_login_request(token))
    except requests.RequestException:
        print("Connectivity error for login post.")
        return quit(0)

    if post_response.status_code != 304:
        print("Unable to successfully login post.")
        return quit(0)


def get_login_request(token: str) -> dict:
    request = LoginConfig.request_template(token)
    while (
        not request["email"]
        or not request["password"]
        or not all(s in request["email"] for s in ("@", "."))
    ):
        print("Email, password: ")
        try:
            request["email"], request["password"] = [
                i_str.strip(" ") for i_str in input().split(",")
            ]
        except ValueError:
            request["email"], request["password"] = "", ""
            continue
    return request
