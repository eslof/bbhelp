from datetime import datetime
import json
from typing import TypedDict, List


class BumpedBook(TypedDict):
    timestamp: int
    book_id: str
    title: str
    author: str


class SaveState(TypedDict):
    day: int
    count: int


class SaveData:
    bumped_books: List[BumpedBook]
    save_state: SaveState

    @staticmethod
    def load():
        with open("save_data.json", "w+") as f:
            content = f.read()
            if content:
                data = json.loads(content)
            else:
                data = {}

            if "bumped_books" in data and data["bumped_books"]:
                SaveData.bumped_books = data["bumped_books"]
            else:
                SaveData.bumped_books = []

            if "save_state" in data and data["bumped_books"]:
                SaveData.save_state = data["save_state"]
            else:
                SaveData.save_state = SaveState(day=datetime.now().weekday(), count=0)

    @staticmethod
    def save():
        with open("save_data.json", "w+") as f:
            f.write(
                json.dumps(
                    {
                        "bumped_books": SaveData.bumped_books,
                        "save_state": SaveData.save_state,
                    }
                )
            )
