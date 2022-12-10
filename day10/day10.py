from typing import List


class ElvenCPU:

    SPECIAL_REGISTERS = {20, 60, 100, 140, 180, 220}

    def __init__(self, program: List[str]) -> None:
        self.program = program
        self.x = 1
        self.cycle = 1

    def execute_program(self) -> int:
        res = 0
        for line in self.program:
            parts = line.split()
            cmd = parts[0]
            if cmd == "noop":
                res += self._increment_cycle(1)
            elif cmd == "addx":
                res += self._increment_cycle(2)
                strength = int(parts[1])
                self.x += strength
            else:
                raise ValueError("Only `noop` and `addx` are supported!")

        return res

    def _increment_cycle(self, iterations: int) -> int:
        signal_strength = 0
        for _ in range(iterations):
            if self.cycle in self.SPECIAL_REGISTERS:
                signal_strength += self.cycle * self.x
            self.cycle += 1

        return signal_strength


def read_input() -> List[str]:
    with open("input.txt") as f:
        contents = [l.strip() for l in f.readlines()]
    return contents


def part_one() -> int:
    program = read_input()
    cpu = ElvenCPU(program=program)
    signal_strength = cpu.execute_program()
    return signal_strength


def part_two():
    return "Not Implemented"


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
