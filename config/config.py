class BookConfig:
    PAGE_URL = "https://www.bokborsen.se/user/product"
    JSON_URL = PAGE_URL + "/list?"

    @staticmethod
    def request_template(request_number: int, count: int, timestamp: int) -> dict:
        return {
            "draw": request_number,
            "columns[0][data]": "",
            "columns[0][name]": "format",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "false",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "external_sku",
            "columns[1][name]": "",
            "columns[1][searchable]": "true",
            "columns[1][orderable]": "true",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "created_at",
            "columns[2][name]": "",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "true",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "",
            "columns[3][name]": "search",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "false",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "usergenre_id",
            "columns[4][name]": "",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "false",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "columns[5][data]": "price",
            "columns[5][name]": "",
            "columns[5][searchable]": "true",
            "columns[5][orderable]": "true",
            "columns[5][search][value]": "",
            "columns[5][search][regex]": "false",
            "columns[6][data]": "free_shipping",
            "columns[6][name]": "",
            "columns[6][searchable]": "true",
            "columns[6][orderable]": "false",
            "columns[6][search][value]": "",
            "columns[6][search][regex]": "false",
            "columns[7][data]": "status",
            "columns[7][name]": "",
            "columns[7][searchable]": "true",
            "columns[7][orderable]": "true",
            "columns[7][search][value]": "enabled",
            "columns[7][search][regex]": "false",
            "columns[8][data]": "id",
            "columns[8][name]": "",
            "columns[8][searchable]": "true",
            "columns[8][orderable]": "false",
            "columns[8][search][value]": "",
            "columns[8][search][regex]": "false",
            "columns[9][data]": "id",
            "columns[9][name]": "",
            "columns[9][searchable]": "true",
            "columns[9][orderable]": "true",
            "columns[9][search][value]": "",
            "columns[9][search][regex]": "false",
            "order[0][column]": "created_at",
            "order[0][dir]": "asc",
            "start": 0,
            "length": count,
            "search[value]": "",
            "search[regex]": "false",
            "_": timestamp,
        }


class BumpConfig:
    ACTION_URL = "https://www.bokborsen.se/user/product/action"

    @staticmethod
    def request_template(ids: list) -> dict:
        return {
            "manage_product_ids": ",".join(ids),
            "product_action[]": "bump",
            "inc": "",
            "dec": "",
        }


class LoginConfig:
    PAGE_URL = "https://www.bokborsen.se/auth/login"
    FORM_NAME = "input"
    TOKEN_NAME = "_token"

    @staticmethod
    def request_template(token: str):
        return {
            "redirect": "",
            "email": "",
            "password": "",
            LoginConfig.TOKEN_NAME: token,
        }


class MainConfig:
    DEFAULT_BOOK_COUNT = 10
    REQUEST_HEADERS = {
        "Accept": "text/html,"
        "application/xhtml+xml,"
        "application/xml;q=0.9,"
        "image/avif,image/webp,"
        "image/apng,"
        "*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,sv;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.bokborsen.se",
        "sec-ch-ua": '"Google Chrome";v="87",'
        ' " Not;A Brand";v="99",'
        ' "Chromium";v="87"',
        "sec-ch-ua-mobile": "?1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
        " AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/87.0.4280.141 Mobile Safari/537.36 ",
    }


class TrackConfig:
    PUBLIC_LISTING_URL = "https://www.bokborsen.se/books"
    LIST_EL = "ul"
    LIST_CLASS = "list list-books"
    ID_EL = "img"
    ID_ATTR = "data-id"
