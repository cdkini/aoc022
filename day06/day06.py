from collections import defaultdict


def read_input() -> str:
    with open("input.txt") as f:
        contents = f.read().strip()
    return contents


def _sliding_window(datastream: str, distinct_char_count: int) -> int:
    seen = defaultdict(int)

    # Set up initial window state
    left, right = 0, 0
    while right < distinct_char_count - 1:
        seen[datastream[right]] += 1
        right += 1
    seen[datastream[right]] += 1

    while right < len(datastream):
        # Remove left-most char from sliding window
        lchar = datastream[left]
        seen[lchar] -= 1
        if seen[lchar] == 0:
            del seen[lchar]
        left += 1

        # Extend window to the right
        right += 1
        rchar = datastream[right]
        seen[rchar] += 1

        # Char count will always be equal to 'distinct_char_count' so we should have
        # an equivalent amount of keys
        if len(seen) == distinct_char_count:
            break

    return right + 1


def part_one() -> int:
    return _sliding_window(datastream=read_input(), distinct_char_count=4)


def part_two() -> int:
    return _sliding_window(datastream=read_input(), distinct_char_count=14)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
