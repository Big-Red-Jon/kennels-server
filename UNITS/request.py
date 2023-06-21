import sqlite3
import json
from models import Unit

UNITS = [
    {
        "id": 1,
        "name": "Stormtroopers",
        "unit_type_id": 3,
        "amount": 4,
        "speed": 2,
        "faction_id": 1,
        "point_cost": 44,
        "owned_amount": 4,
        "health": 1,
        "courage": 1,
        "defense_dice_id": 2,
        "surge_to_hit": True,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "weapon_id": [1, 2],
        "keyword_id": 1,
        "upgrade_id": [1, 2, 3],
        "unit_img": "https://static.wikia.nocookie.net/starwarslegion/images/8/80/Swl01_unit_stormtrooper.png/revision/latest?cb=20171231012659"
    },
    {
        "id": 2,
        "name": "Shoretroopers",
        "unit_type_id": 3,
        "amount": 4,
        "speed": 2,
        "faction_id": 1,
        "point_cost": 52,
        "owned_amount": 2,
        "health": 1,
        "courage": 1,
        "defense_dice_id_id": 2,
        "surge_to_hit": False,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "keyword_id": [3, 4],
        "weapon_id": [1, 2],
        "upgrade_id": [1, 2, 3],
        "unit_img": "https://starwarslegion.fandom.com/wiki/Shoretroopers?file=Shoretroopers.png"
    },
    {
        "id": 2,
        "name": "Snowtroopers",
        "unit_type_id": 3,
        "amount": 4,
        "speed": 1,
        "faction_id": 1,
        "point_cost": 52,
        "owned_amount": 2,
        "health": 1,
        "courage": 1,
        "defense_dice_id_id": 2,
        "surge_to_hit": False,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "keyword_id": 2,
        "weapon_id": [1, 2],
        "upgrade_id": [1, 2, 3],
        "unit_img": "https://starwarslegion.fandom.com/wiki/Snowtroopers?file=Snowtroopers_new.png"
    }
]


def get_all_units():

    with sqlite3.connect("./legion.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.name,
            u.unit_type_id,
            u.amount,
            u.speed,
            u.faction_id,
            u.point_cost,
            u.owned_amount,
            u.health,
            u.courage,
            u.defense_dice_id,
            u.surge_to_hit,
            u.surge_to_crit,
            u.surge_to_defend,
            u.keyword_id,
            u.weapon_id,
            u.upgrade_id
        FROM unit u
        """)

        units = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            unit = Unit(row['id'], row['name'], row['unit_type_id'],
                        row['amount'], row['speed'], row['faction_id'],
                        row['point_cost'], row['owned_amount'], row['health'],
                        row['courage'], row['defense_dice_id'], row['surge_to_hit'], row['surge_to_crit'], row[
                'surge_to_defend'], row['keyword_id'], row['weapon_id'], row['upgrade_id']
            )

            units.append(units.__dict__)

    return json.dumps(units)


def get_single_unit(id):
    requested_unit = None

    for unit in UNITS:
        if unit["id"] == id:
            requested_unit = unit
    return requested_unit
