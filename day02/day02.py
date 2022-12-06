from typing import List, Tuple


def read_input() -> List[Tuple[str, str]]:
    with open("input.txt") as f:
        contents = f.readlines()
    return [tuple(line.split()) for line in contents]


def part_one() -> int:
    total = 0
    for x, y in read_input():
        if y == "X":
            total += 1
            if x == "A":
                total += 3
            elif x == "B":
                total += 0
            else:
                total += 6
        elif y == "Y":
            total += 2
            if x == "A":
                total += 6
            elif x == "B":
                total += 3
            else:
                total += 0
        else:
            total += 3
            if x == "A":
                total += 0
            elif x == "B":
                total += 6
            else:
                total += 3

    return total


def part_two() -> int:
    total = 0
    for x, y in read_input():
        if y == "X":
            if x == "A":
                total += 3
            elif x == "B":
                total += 1
            else:
                total += 2
        elif y == "Y":
            total += 3
            if x == "A":
                total += 1
            elif x == "B":
                total += 2
            else:
                total += 3
        else:
            total += 6
            if x == "A":
                total += 2
            elif x == "B":
                total += 3
            else:
                total += 1

    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
