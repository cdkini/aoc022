from __future__ import annotations

from typing import Dict, List, Optional


class AoCFile:
    def __init__(
        self,
        name: str,
        is_dir: bool,
        children: Optional[Dict[str, AoCFile]] = None,
        parent: Optional[AoCFile] = None,
        size: int = 0,
    ) -> None:
        self.name = name
        self.is_dir = is_dir
        self.children = children or {}
        self.parent = parent
        self.size = size


class FilesystemEvaluator:
    def __init__(self, logs: List[str]) -> None:
        self.root = AoCFile(name="/", is_dir=True)
        self.ptr = self.root
        self._traverse_filesystem(logs)

    def determine_total_size_over_threshold(self, threshold: int) -> int:
        res = 0
        stack = [self.root]
        while stack:
            node = stack.pop()

            # If evaluating a dir, save for later processing
            if node.is_dir and node.size <= threshold:
                res += node.size

            # DFS let's us evaluate deepest nodes first
            for child in node.children.values():
                stack.append(child)

        return res

    def determine_necessary_dir_deletion(
        self, necessary_disk_space: int, total_disk_space: int
    ) -> AoCFile:
        unused_disk_space = total_disk_space - self.root.size
        space_to_free = necessary_disk_space - unused_disk_space

        res = self.root

        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node.is_dir:
                continue

            # Diff must be greater than zero to be a valid selection
            diff = node.size - space_to_free
            if diff >= 0 and diff < res.size - space_to_free:
                res = node

            for child in node.children.values():
                stack.append(child)

        return res

    def _traverse_filesystem(self, logs: List[str]) -> None:
        for line in logs:
            parts = line.split()
            if parts[0] == "$":
                self._evaluate_command(parts=parts)
            else:
                self._evaluate_ls_output(parts=parts)

    def _evaluate_command(self, parts: List[str]) -> None:
        if parts[1] == "cd":
            dest = parts[2]
            if dest == "/":
                self.ptr = self.root
            elif dest == "..":
                self.ptr = self.ptr.parent
            else:
                self.ptr = self.ptr.children[dest]
        elif parts[1] == "ls":
            pass  # The actual call to `ls` doesn't impact our pointer at all
        else:
            raise ValueError("Input should only include `cd` and `ls`")

    def _evaluate_ls_output(self, parts: List[str]) -> None:
        size, name = parts
        if size == "dir":
            f = AoCFile(name=name, is_dir=True, parent=self.ptr)
        else:
            size = int(size)
            f = AoCFile(name=name, is_dir=False, parent=self.ptr, size=size)
            # Update all parents up to the root whenever we find a file
            tmp = self.ptr
            while tmp:
                tmp.size += size
                tmp = tmp.parent

        self.ptr.children[name] = f


def read_input() -> List[str]:
    with open("input.txt") as f:
        contents = [l.strip() for l in f.readlines()]
    return contents


def part_one():
    logs = read_input()
    fse = FilesystemEvaluator(logs)
    return fse.determine_total_size_over_threshold(threshold=100_000)


def part_two():
    logs = read_input()
    fse = FilesystemEvaluator(logs)
    dir_to_delete = fse.determine_necessary_dir_deletion(
        necessary_disk_space=30_000_000, total_disk_space=70_000_000
    )
    return dir_to_delete.size


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
