import sqlite3
import json

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
    return FACTIONS


def get_single_faction(id):
    requested_faction = None

    for faction in FACTIONS:
        if faction["id"] == id:
            requested_faction = faction
            return requested_faction
