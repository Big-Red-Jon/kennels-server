
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
        "defense_dice": 2,
        "surge_to_hit": True,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "weaponId": [1, 2],
        "keyword_id": 1,
        "upgrade_id": [1, 2, 3],
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
        "defense_dice": 2,
        "surge_to_hit": False,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "keyword_id": [3, 4],
        "weaponId": [1, 2],
        "upgrade_id": [1, 2, 3],
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
        "defense_dice": 2,
        "surge_to_hit": False,
        "surge_to_crit": False,
        "surge_to_defend": False,
        "keyword_id": 2,
        "weaponId": [1, 2],
        "upgrade_id": [1, 2, 3],
    }
]


def get_all_units():
    return UNITS


def get_single_unit(id):
    requested_unit = None

    for unit in UNITS:
        if unit["id"] == id:
            requested_unit = unit
    return requested_unit
