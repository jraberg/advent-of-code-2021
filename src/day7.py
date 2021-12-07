from collections import defaultdict
from typing import List, Dict

from src.file_utils import read_data


def parse(raw) -> List[int]:
    return [int(n) for n in raw.split(',')]


def mk_cost_tbl(highest_pos: int):
    cost_tbl = defaultdict(int)
    for align_pos in range(highest_pos):
        for pos in range(highest_pos):
            cost_tbl[(pos, align_pos)] = sum(range(1, abs(align_pos - pos) + 1))


def cost_position(align_pos: int, initial_pos: List[int], cost_tbl: Dict[int, int]) -> int:
    cost = []
    for pos in initial_pos:
        cost.append(cost_tbl[abs(align_pos - pos)])
    return sum(cost)


def cost_position2(align_pos: int, initial_pos: List[int], cost_tbl: Dict[int, int]) -> int:
    cost = []
    for pos in initial_pos:
        no_steps = abs(align_pos - pos)
        if no_steps not in cost_tbl.keys():
            cost_tbl[no_steps] = sum(range(1, no_steps + 1))
        cost.append(cost_tbl[no_steps])
    return sum(cost)


def solve_part1(raw: str):
    positions = parse(raw)
    highest_pos = max(positions)
    cost_tbl = {i: i for i in range(highest_pos + 1)}
    costs = defaultdict(int)
    for base in range(highest_pos):
        costs[base] = cost_position(base, positions, cost_tbl)
    return min(costs.values())


def solve_part2(raw: str):
    positions = parse(raw)
    highest_pos = max(positions)
    cost_tbl = defaultdict(int)
    costs = defaultdict(int)
    for base in range(highest_pos):
        costs[base] = cost_position2(base, positions, cost_tbl)
    return min(costs.values())


def main():
    raw = read_data("day7.txt")
    solution_part1: int = solve_part1(raw)
    print(f"Day 7 -> part 1: {solution_part1}")
    solution_part2: int = solve_part2(raw)
    print(f"Day 7 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
