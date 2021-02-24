def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with{expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


# How first class functions can be useful

def get_friend_name(friend):
    return friend["name"]


# the get_friend_name finder will run the finder on every element in friends.
print(search(friends, "Rolf Smith", get_friend_name))
