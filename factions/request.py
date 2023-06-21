import sqlite3
import json
from models import Faction

FACTIONS = [
    {
        "id": 1,
        "name": "Empire"
    },
    {
        "id": 2,
        "name": "Rebellion"
    },
    {
        "id": 3,
        "name": "Republic"
    },
    {
        "id": 4,
        "name": "Separatists"
    },
    {
        "id": 5,
        "name": "Shadow Collective"
    }
]


def get_all_factions():
    with sqlite3.connect("./legion.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            f.id,
            f.name
        FROM faction f
        """)

        factions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            faction = Faction(row["id"], row["name"]
                              )
            factions.append(factions.__dict__)

    return json.dumps(factions)


def get_single_faction(id):
    requested_faction = None

    for faction in FACTIONS:
        if faction["id"] == id:
            requested_faction = faction
            return requested_faction
