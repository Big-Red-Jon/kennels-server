LISTS = [
    {
        "id":  1,
        "commander_id": 1,
        "operative_id": 1,
        "corps_id": [1, 2, 3],
        "special_forces_id": [2, 2],
        "support_id": [1, 1],
        "heavy_id": 1
    },
    {
        "id":  2,
        "commander_id": 2,
        "operative_id": 1,
        "corps_id": [1, 2, 3],
        "special_forces": [2, 2],
        "support_id": [1, 1],
        "heavy_id": 1
    },
    {
        "id":  3,
        "commander_id": 2,
        "operative_id": 1,
        "corps_id": [1, 2, 3],
        "special_forces_id": [2, 2],
        "support_id": [1, 1],
        "heavy_id": 1
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


def delete_list(id):
    list_index = -1
    for index, list in enumerate(LISTS):
        if list["id"] == id:
            list_index = index
    if list_index >= 0:
        LISTS.pop(list_index)


def update_list(id, new_list):
    for index, list in enumerate(LISTS):
        if list["id"] == id:
            LISTS[index] = new_list
            break


#  {
#         "id":  1,
#         "commander_id": 1,
#         "operative_id": 1,
#         "corps_id": [1, 1, 1],
#         "special_forces_id": [1, 1],
#         "support_id": [1, 1],
#         "heavy_id_id": 1
# }
