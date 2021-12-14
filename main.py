import random
import time

from requests import Session

from data.save_data import SaveData, BumpedBook
from model.book import get_oldest
from model.bump import do_bump
from model.login import do_login
from model.schedule import Schedule
from config.config import MainConfig, BookConfig


def main():
    with Session() as s:
        s.headers = MainConfig.REQUEST_HEADERS
        do_login(s)

        SaveData.load()
        request_number = 0
        s.get(
            BookConfig.PAGE_URL
        )  # doesn't have to be here, just keeping up appearances
        while True:
            timestamp = int(time.time())
            if not Schedule.should_bump(s, timestamp, 15):
                time.sleep(30 + (random.random() * 30))
                continue

            # Get oldest, bump oldest
            request_number += 1
            target_book = get_oldest(
                s, request_number, MainConfig.DEFAULT_BOOK_COUNT, timestamp
            )[0]
            book_id, title, author = (
                target_book["id"],
                target_book["title"],
                target_book["author"],
            )

            do_bump(s, [book_id])

            # Save state
            SaveData.save_state["count"] += 1
            SaveData.bumped_books.append(
                BumpedBook(
                    timestamp=timestamp, book_id=book_id, title=title, author=author
                )
            )
            SaveData.save()


if __name__ == "__main__":
    main()
