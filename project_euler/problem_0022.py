# https://projecteuler.net/problem=22


def get_names() -> list[str]:
    with open("data/22.txt", "r") as f:
        names = [name[1:-1] for name in f.read().split(",")]
        return names


names = sorted(get_names())

letters = {
    char: ord(char) - 64
    for char in [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
}


def get_alphabetical_sum(name: str) -> int:
    alphabetical_sum = 0
    for c in name:
        alphabetical_sum += letters[c]

    return alphabetical_sum


total = 0
for i, name in enumerate(names):
    alphabetical_sum = get_alphabetical_sum(name)
    position = i + 1
    total += alphabetical_sum * position

print(total)
