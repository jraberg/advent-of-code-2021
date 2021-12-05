import math
import re
from dataclasses import dataclass
from typing import List, NamedTuple, Tuple
from collections import Counter

from src.file_utils import read_data


def parse_vents(vents: str, diag_lines: bool = False):
    start, end = re.split(r'\W+\->\W+', vents)
    x1, y1 = parse_position(start)
    x2, y2 = parse_position(end)
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield x1, y
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y1
    if abs(y2 - y1) == abs(x2 - x1) and diag_lines:
        x_step = 1 if x2 > x1 else -1
        y_step = 1 if y2 > y1 else -1
        for x, y in zip(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)):
            yield x, y


class Position(NamedTuple):
    x: int
    y: int
    count: int

    def has_multiple_vents(self, threshold: int = 2):
        return self.count >= threshold


@dataclass
class Map:
    vents: List[Position]

    def points_multiple_vents(self, threshold: int = 2):
        return [p for p in self.vents if p.has_multiple_vents()]

    @staticmethod
    def parse(raw: str, diag: bool = False):
        positions = []
        for l in parse(raw):
            for position in parse_vents(l, diag):
                positions.append(position)
        return Map([Position(p[0], p[1], c) for p, c in Counter(positions).items()])


def parse_position(pos: str) -> Tuple[int, int]:
    x, y = pos.split(',')
    return int(x), int(y)


def parse(raw: str) -> List[str]:
    return [p for p in raw.split('\n')]


def solve_part1(raw: str):
    m = Map.parse(raw)
    return len(m.points_multiple_vents())


def solve_part2(raw: str):
    m = Map.parse(raw, True)
    return len(m.points_multiple_vents())


def main():
    raw = read_data("day5.txt")
    solution_part1: int = solve_part1(raw)
    print(f"Day 5 -> part 1: {solution_part1}")
    solution_part2: int = solve_part2(raw)
    print(f"Day 5 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
