LISTS = [
    {
        "id":  1,
        "commander": 1,
        "operative": 1,
        "corps": [1, 2, 3],
        "specialForces": [2, 2],
        "support": [1, 1],
        "heavy": 1
    },
    {
        "id":  2,
        "commander": 2,
        "operative": 1,
        "corps": [1, 2, 3],
        "specialForces": [2, 2],
        "support": [1, 1],
        "heavy": 1
    },
    {
        "id":  3,
        "commander": 2,
        "operative": 1,
        "corps": [1, 2, 3],
        "specialForces": [2, 2],
        "support": [1, 1],
        "heavy": 1
    }
]


def get_all_lists():
    return LISTS


def get_single_list(id):
    requested_list = None

    for list in LISTS:
        if list["id"] == id:
            requested_list = list
        return requested_list


def create_list(list):
    max_id = LISTS[-1]["id"]
    new_id = max_id+1
    list["id"] = new_id
    LISTS.append(list)
    return list
