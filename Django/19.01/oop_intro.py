import os

os.system('cls' if os.name == "nt" else "clear")


def print_type(data):
    for i in data:
        print(i, type(i))


test = [123, 'Barry', [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x, {
    "name": "Barry", "age": 44}]

print_type(test)

