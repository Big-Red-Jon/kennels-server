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
    return DEFENSEDICE


def get_single_defense_dice(id):
    requested_dice = None

    for dice in DEFENSEDICE:
        if dice["id"] == id:
            requested_dice = dice
            return requested_dice
