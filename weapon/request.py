WEAPONS = [
    {
        "id": 1,
        "name": "Force Lightning",
        "black_dice": 2,
        "red_dice": 2,
        "white_dice": 2,
        "keyword_id": [15, 21],
        "range": ["0", "1-2"],
        "unique_weapon": True
    },
    {
        "id": 2,
        "name": "Vader's Lightsaber-Commander",
        "black_dice": 0,
        "red_dice": 6,
        "white_dice": 0,
        "keyword_id": 15,
        "range": "0",
        "unique_weapon": True
    }
]


def get_all_weapons():
    return WEAPONS


def get_single_weapon(id):
    requested_weapon = None
    for weapon in WEAPONS:
        if weapon["id"] == id:
            requested_weapon = weapon
            return requested_weapon
