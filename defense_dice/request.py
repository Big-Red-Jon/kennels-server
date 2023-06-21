import sqlite3
import json
from models import DefenseDice

DEFENSEDICE = [
    {
        "id": 1,
        "color": "red"
    },
    {
        "id": 2,
        "color": "white"
    }
]


def get_all_defense_dice():
    with sqlite3.connect("./legion.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.color
        FROM defensedice d
        """)

        defensedice = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            defensedie = DefenseDice(row["id"], row["color"]
                                     )
            defensedice.append(defensedice.__dict__)

    return json.dumps(defensedice)


def get_single_defense_dice(id):
    requested_dice = None

    for dice in DEFENSEDICE:
        if dice["id"] == id:
            requested_dice = dice
            return requested_dice
