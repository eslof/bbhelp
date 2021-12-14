from datetime import datetime
import json
from typing import Dict, TypedDict

import requests

from data.save_data import SaveData, SaveState
from model.track import get_position


class Day(TypedDict):
    start: int
    end: int
    limit: int


class Schedule:
    day_info: Dict[int, Day]

    @staticmethod
    def load():
        with open("save_data.json", "w+") as f:
            content = f.read()
            if content:
                data = json.loads(content)
            else:
                data = {}

            if "day_info" in data and data["day_info"]:
                Schedule.day_info = data["day_info"]
            else:
                print("No schedule found.")
                quit(0)

    @staticmethod
    def should_bump(s: requests.Session, timestamp: int, cutoff: int) -> bool:
        current_day = datetime.now().weekday()
        save_day = SaveData.save_state["day"]
        day_info = Schedule.day_info[current_day]

        if save_day != current_day:
            SaveData.save_state = SaveState(day=current_day, count=0)

        count = SaveData.save_state["count"]

        if (
            not day_info["start"] < timestamp < day_info["end"]
            or count >= day_info["limit"]
        ):
            return False

        if SaveData.bumped_books:
            last_bump = SaveData.bumped_books[-1]
            if 0 <= get_position(s, last_bump["book_id"]) <= cutoff:
                return False

        return True
