import sqlite3
import json

UPGRADE = [
    {
        "id": 1,
        "type": "Armament",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 2,
        "type": "Command",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 3,
        "type": "Comms",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 4,
        "type": "Crew",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 5,
        "type": "Force",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 6,
        "type": "Gear",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 7,
        "type": "Generator",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 8,
        "type": "Grenades",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 9,
        "type": "Hardpoint",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 10,
        "type": "Heavy Weapon",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 11,
        "type": "Ordnance",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 12,
        "type": "Personnel",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 13,
        "type": "Pilot",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 14,
        "type": "Protocol",
        "card_id": 0,
        "keyword_id": 0
    },
    {
        "id": 15,
        "type": "Training",
        "card_id": 0,
        "keyword_id": 0
    },
]


def get_all_upgrades():
    return UPGRADE


def get_single_upgrade(id):
    requested_upgrade = None

    for upgrade in UPGRADE:
        if upgrade["id"] == id:
            requested_upgrade = upgrade
            return requested_upgrade
