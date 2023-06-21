import sqlite3
import json

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
    return UNITTYPES


def get_single_unitType(id):
    requested_unitType = None

    for unitType in UNITTYPES:
        if unitType["id"] == id:
            requested_unitType = unitType
    return requested_unitType
