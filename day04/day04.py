import re
from typing import List, Tuple

Assignment = Tuple[Tuple[int, int], Tuple[int, int]]

r = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def read_input():
    with open("input.txt") as f:
        contents = [l.strip() for l in f.readlines()]
    return contents


def _construct_assignments(
    raw_input: List[str],
) -> List[Assignment]:
    assignments = []
    for line in raw_input:
        matches = r.match(line)
        groups = matches.groups()
        assignment = (
            (int(groups[0]), int(groups[1])),
            (int(groups[2]), int(groups[3])),
        )
        assignments.append(assignment)
    return assignments


def _does_fully_contain(assignment: Assignment) -> bool:
    a1, a2 = assignment
    return (a1[0] <= a2[0] and a1[1] >= a2[1]) or (a2[0] <= a1[0] and a2[1] >= a1[1])


def part_one():
    raw_input = read_input()
    assignments = _construct_assignments(raw_input)
    return sum(1 for assignment in assignments if _does_fully_contain(assignment))


def _does_overlap(assignment: Assignment) -> bool:
    a1, a2 = assignment
    if a1[0] < a2[0]:
        return a1[1] >= a2[0]
    return a2[1] >= a1[0]


def part_two():
    raw_input = read_input()
    assignments = _construct_assignments(raw_input)
    return sum(1 for assignment in assignments if _does_overlap(assignment))


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
