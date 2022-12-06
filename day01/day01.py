def read_input():
    with open("input.txt") as f:
        contents = f.readlines()

    res, curr = [], []
    for line in contents:
        line = line.strip()
        if not line:
            res.append(curr)
            curr = []
        else:
            curr.append(int(line))

    return res


def part_one():
    max_elf = 0
    for elf in read_input():
        max_elf = max(max_elf, sum(elf))
    return max_elf


def part_two():
    max_elves = [0, 0, 0]

    for elf in read_input():
        val = sum(elf)
        if val > max_elves[0]:
            max_elves[2] = max_elves[1]
            max_elves[1] = max_elves[0]
            max_elves[0] = val
        elif val > max_elves[1]:
            max_elves[2] = max_elves[1]
            max_elves[1] = val
        elif val > max_elves[2]:
            max_elves[2] = val

    return sum(max_elves)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
