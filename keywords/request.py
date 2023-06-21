import sqlite3
import json
from models import Keywords

KEYWORDS = [
    {
        "id": 1,
        "title": "Arm",
        "description": "A unit that is equipped with a card that has the Arm X: Charge Token Type keyword can perform the Arm X action. When a unit performs the Arm X action, the unit places X charge tokens of the specific type and matching its controlling player’s color within range 1 and LOS of its unit leader. Charge tokens cannot overlap any objective, condition, or other charge tokens and must be placed on flat surface completely flush with that surface.",
        "type": "Weapon"
    },
    {
        "id": 2,
        "title": "Beam",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 3,
        "title": "Blast",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 4,
        "title": "Critical",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 5,
        "title": "Cumbersome",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 6,
        "title": "Detonate",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 7,
        "title": "Fixed: Front/Rear",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 8,
        "title": "High Velocity",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 9,
        "title": "Immobilize",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 10,
        "title": "Immune: Deflect",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 11,
        "title": "Ion",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 12,
        "title": "Lethal",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 13,
        "title": "Long Shot",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 14,
        "title": "Overrun",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 15,
        "title": "Pierce",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 16,
        "title": "Poison",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 17,
        "title": "Ram",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 18,
        "title": "Self Destruct",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 19,
        "title": "Scatter",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 20,
        "title": "Spray",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 21,
        "title": "Suppressive",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 22,
        "title": "Tow Cable",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 23,
        "title": "Versatile",
        "description": "",
        "type": "Weapon"
    },
    {
        "id": 24,
        "title": "Bane Tokens",
        "description": "",
        "type": "Command Card"
    },
    {
        "id": 25,
        "title": "Cycle",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 26,
        "title": "Divulge",
        "description": "",
        "type": "Command Card"
    },
    {
        "id": 27,
        "title": "Graffiti Tokens",
        "description": "",
        "type": "Command Card"
    },
    {
        "id": 28,
        "title": "Leader",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 29,
        "title": "NonCombatant",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 30,
        "title": "Permanent",
        "description": "",
        "type": "Command Card"
    },
    {
        "id": 31,
        "title": "Reconfigure",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 32,
        "title": "Repair: Capacity",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 33,
        "title": "SideArm: melee/ranged",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 34,
        "title": "Small",
        "description": "",
        "type": "Upgrade"
    },
    {
        "id": 35,
        "title": "Treat: Capacity",
        "description": "",
        "type": "Upgrade"
    },

]


def get_all_keywords():

    with sqlite3.connect("./legion.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            k.id,
            k.title,
            k.description,
            k.type
        FROM keywords k
        """)

        keywords = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            keyword = Keywords(row["id"], row["title"], row["description"], row["type"]
                               )
            keywords.append(keywords.__dict__)

    return json.dumps(keywords)


def get_single_keyword(id):
    requested_keyword = None
    for keyword in KEYWORDS:
        if keyword["id"] == id:
            requested_keyword = keyword
        return requested_keyword
