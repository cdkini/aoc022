import enum
from dataclasses import dataclass
from typing import List

GRID_DIMENSIONS = 10


class Direction(enum.Enum):
    LEFT = "L"
    RIGHT = "R"
    UP = "U"
    DOWN = "D"


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Instruction:
    direction: Direction
    steps: int


class Simulation:
    def __init__(self, dimensions: int) -> None:
        # Start head/tail in a safe space in the middle of the grid
        x = dimensions // 2
        y = x
        x, y = 0, 0
        self.head = Coordinates(x=x, y=y)
        self.tail = Coordinates(x=x, y=y)
        self.visited = [[0 for _ in range(dimensions)] for _ in range(dimensions)]

    def simulate(self, instructions: List[Instruction]) -> int:
        for instruction in instructions:
            self._move_rope(instruction)

        return self._calculate_visits()

    def _calculate_visits(self) -> int:
        visits = 0
        for r in range(len(self.visited)):
            for c in range(len(self.visited[0])):
                if self.visited[r][c] > 0:
                    visits += 1

        return visits

    def _move_rope(self, instruction: Instruction) -> None:
        direction, steps = instruction.direction, instruction.steps
        for _ in range(steps):
            self._move_head(direction)
            self._move_tail()

    def _move_head(self, direction: Direction) -> None:
        xd, yd = 0, 0
        if direction is Direction.LEFT:
            xd -= 1
        elif direction is Direction.RIGHT:
            xd += 1
        elif direction is Direction.UP:
            yd += 1
        else:
            yd -= 1

        self.head.x += xd
        self.head.y += yd

    def _move_tail(self) -> None:
        xd = self.head.x - self.tail.x
        yd = self.head.y - self.tail.y

        if (abs(xd) == 1 and abs(yd) != 1) or (abs(xd) != 1 and abs(yd) == 1):
            return

        # If both dimensions have changed, we know we need diagonal movement
        complex = xd != 0 and yd != 0
        if complex:
            self._process_complex_tail_movement(xd=xd, yd=yd)
        else:
            self._process_simple_tail_movement(xd=xd, yd=yd)

        self._mark_visited()

    def _process_complex_tail_movement(self, xd: int, yd: int) -> None:
        if xd < 0:
            xd = -1
        else:
            xd = 1

        if yd < 0:
            yd = -1
        else:
            yd = 1

        self.tail.x += xd
        self.tail.y += yd

    def _process_simple_tail_movement(self, xd: int, yd: int) -> None:
        if xd > 0:
            self.tail.x += 1
        elif xd < 0:
            self.tail.x -= 1
        elif yd > 0:
            self.tail.y += 1
        else:
            self.tail.y -= 1

    def _mark_visited(self) -> None:
        x, y = self.tail.x, self.tail.y
        self.visited[x][y] += 1


def read_input() -> List[str]:
    with open("input.txt") as f:
        contents = [l.strip() for l in f.readlines()]
    return contents


def _parse_instructions(raw_input: List[str]) -> List[Instruction]:
    instructions = []
    for line in raw_input:
        direction, steps = line.split()
        instruction = Instruction(direction=Direction(direction), steps=int(steps))
        instructions.append(instruction)
    return instructions


def part_one():
    breakpoint()
    raw_input = read_input()
    instructions = _parse_instructions(raw_input)
    simulation = Simulation(GRID_DIMENSIONS)
    return simulation.simulate(instructions)


def part_two():
    return "Not Implemented"


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
