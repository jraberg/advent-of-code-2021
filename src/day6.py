from collections import defaultdict, Counter
from typing import List

from src.file_utils import read_data


def parse(raw) -> List[int]:
    return [int(n) for n in raw.split(',')]


def solve(raw: str, days: int):
    fish_counter = [0] * 9
    fishes = [int(fish) for fish in raw.split(',')]
    for fish in fishes:
        fish_counter[fish] += 1
    for day in range(days):
        cur_fish_count = fish_counter.pop(0)
        fish_counter.append(cur_fish_count)
        fish_counter[6] += cur_fish_count
    return sum(fish_counter)


def main():
    raw = read_data("day6.txt")
    raw = """3,4,3,1,2"""
    solution_part1: int = solve(raw, 80)
    print(f"Day 6 -> part 1: {solution_part1}")
    solution_part2: int = solve(raw, 256)
    print(f"Day 6 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
