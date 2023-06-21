import sqlite3
import json
from models import UnitType

UNITTYPES = [
    {
        "id": 1,
        "description": "Commander"
    },
    {
        "id": 2,
        "description": "Operative"
    },
    {
        "id": 3,
        "description": "Corps"
    },
    {
        "id": 4,
        "description": "Special Forces"
    },
    {
        "id": 5,
        "description": "Support"
    },
    {
        "id": 6,
        "description": "Heavy"
    }
]


def get_all_unitTypes():
    with sqlite3.connect("/legion.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.description    
        FROM unitType u         
        """)

        unitTypes = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            unittype = UnitType(row['id'], row['description']
                                )

            unitTypes.append(unitTypes.__dict__)

    return json.dumps(unitTypes)


def get_single_unitType(id):
    requested_unitType = None

    for unitType in UNITTYPES:
        if unitType["id"] == id:
            requested_unitType = unitType
    return requested_unitType
