import re
from typing import Dict, List, NamedTuple


class Instruction(NamedTuple):
    count: int
    origin: int
    destination: int


def read_input() -> str:
    with open("input.txt") as f:
        contents = f.read().strip()
    return contents


def _parse_initial_stacks(raw_input: str) -> Dict[int, List[str]]:
    r = re.compile(r"\[(\w)\]")

    stacks = {n: [] for n in range(1, 10)}
    relevant_lines = raw_input.splitlines()[:8]
    for line in relevant_lines:
        matches = r.finditer(line)
        for match in matches:
            char = match.group(1)
            span = match.span()
            pos = (span[0] // 4) + 1
            stacks[pos].append(char)

    for stack in stacks.values():
        stack.reverse()

    return stacks


def _parse_instructions(raw_input: str) -> List[Instruction]:
    r = re.compile(r"move (\d+) from (\d+) to (\d+)")

    instructions = []
    for match in r.finditer(raw_input):
        count, origin, destination = match.groups()
        instruction = Instruction(
            count=int(count), origin=int(origin), destination=int(destination)
        )
        instructions.append(instruction)

    return instructions


def _execute_pt1_instructions(
    instructions: List[Instruction], stacks: Dict[int, List[str]]
) -> str:
    for count, origin, destination in instructions:
        for _ in range(count):
            stacks[destination].append(stacks[origin].pop())

    return _determine_answer(stacks)


def _determine_answer(stacks: Dict[int, List[str]]) -> str:
    res = []
    for stack in stacks.values():
        res.append(stack[-1])
    return "".join(r for r in res)


def part_one():
    raw_input = read_input()
    stacks = _parse_initial_stacks(raw_input)
    instructions = _parse_instructions(raw_input)
    return _execute_pt1_instructions(instructions=instructions, stacks=stacks)


def _execute_pt2_instructions(
    instructions: List[Instruction], stacks: Dict[int, List[str]]
) -> str:
    for count, origin, destination in instructions:
        crates = []
        for _ in range(count):
            crates.append(stacks[origin].pop())
        crates.reverse()
        stacks[destination].extend(crates)

    return _determine_answer(stacks)


def part_two():
    raw_input = read_input()
    stacks = _parse_initial_stacks(raw_input)
    instructions = _parse_instructions(raw_input)
    return _execute_pt2_instructions(instructions=instructions, stacks=stacks)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
