import string
from typing import List, Tuple

SCORE_MAP = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}


def read_input() -> List[str]:
    with open("input.txt") as f:
        contents = [l.strip() for l in f.readlines()]
    return contents


def _eval_compartment(compartment: str) -> int:
    c1 = set(compartment[: len(compartment) // 2])
    c2 = set(compartment[len(compartment) // 2 :])
    return sum(SCORE_MAP[letter] for letter in c1.intersection(c2))


def part_one():
    compartments = read_input()
    return sum(_eval_compartment(compartment) for compartment in compartments)


def _group_compartments(compartments: List[str]) -> List[Tuple[str, str, str]]:
    return list(zip(*(iter(compartments),) * 3))


def _eval_grouped_compartments(grouped_compartments: Tuple[str, str, str]) -> int:
    c1, c2, c3 = grouped_compartments
    c1, c2, c3 = set(c1), set(c2), set(c3)
    return sum(SCORE_MAP[letter] for letter in c1.intersection(c2).intersection(c3))


def part_two():
    compartments = read_input()
    grouped_compartments = _group_compartments(compartments)
    return sum(
        _eval_grouped_compartments(grouped_compartment)
        for grouped_compartment in grouped_compartments
    )


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
