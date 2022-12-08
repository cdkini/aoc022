from typing import List, Tuple


class Forest:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def determine_visible_tree_count(self) -> int:
        visible = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                if self._evaluate_tree_visibility(r=r, c=c):
                    visible += 1

        return visible

    def determine_highest_scenic_score(self) -> int:
        highest = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                highest = max(self._evaluate_tree_score(r=r, c=c), highest)

        return highest

    def _evaluate_tree_visibility(self, r: int, c: int) -> bool:
        # Exit early if on the edge of the matrix
        if (
            r == 0
            or r == len(self.matrix) - 1
            or c == 0
            or c == len(self.matrix[0]) - 1
        ):
            return True

        fns = (self._check_left, self._check_right, self._check_up, self._check_down)
        for fn in fns:
            _, visible = fn(r=r, c=c)
            if visible:
                return True
        return False

    def _evaluate_tree_score(self, r: int, c: int) -> int:
        score = 1
        fns = (self._check_left, self._check_right, self._check_up, self._check_down)
        for fn in fns:
            _score, _ = fn(r=r, c=c)
            score *= _score
        return score

    def _check_left(self, r: int, c: int) -> Tuple[int, bool]:
        count = 0
        for i in range(c - 1, -1, -1):
            count += 1
            if self.matrix[r][i] >= self.matrix[r][c]:
                return count, False
        return count, True

    def _check_right(self, r: int, c: int) -> Tuple[int, bool]:
        count = 0
        for i in range(c + 1, len(self.matrix[0])):
            count += 1
            if self.matrix[r][i] >= self.matrix[r][c]:
                return count, False
        return count, True

    def _check_up(self, r: int, c: int) -> Tuple[int, bool]:
        count = 0
        for i in range(r - 1, -1, -1):
            count += 1
            if self.matrix[i][c] >= self.matrix[r][c]:
                return count, False
        return count, True

    def _check_down(self, r: int, c: int) -> Tuple[int, bool]:
        count = 0
        for i in range(r + 1, len(self.matrix)):
            count += 1
            if self.matrix[i][c] >= self.matrix[r][c]:
                return count, False
        return count, True


def read_input() -> List[List[int]]:
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    contents = []
    for line in lines:
        row = []
        for num in line:
            row.append(int(num))
        contents.append(row)
    return contents


def part_one() -> int:
    matrix = read_input()
    forest = Forest(matrix)
    return forest.determine_visible_tree_count()


def part_two():
    matrix = read_input()
    forest = Forest(matrix)
    return forest.determine_highest_scenic_score()


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
