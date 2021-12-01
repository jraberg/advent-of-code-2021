from typing import List

from src.file_utils import read_data


def solve_part1(raw: List[int]) -> int:
    return sum([1 for a, b in zip(raw, raw[1:]) if a < b])


def is_increasing(a, b, c, d) -> bool:
    sum1 = a + b + c
    sum2 = b + c + d
    return sum1 < sum2


def solve_part2(raw: List[int]) -> int:
    it = iter(raw)
    a, b, c, d = next(it), next(it), next(it), next(it)
    increase = 1 if is_increasing(a, b, c, d) else 0
    for v in it:
        a, b, c, d = b, c, d, v
        if is_increasing(a, b, c, d):
            increase += 1
    return increase


def parse_data(raw: str) -> List[int]:
    return [int(m) for m in raw.split('\n')]


def main():
    raw = read_data("day1.txt")
    data = parse_data(raw)
    solution_part1: int = solve_part1(data)
    solution_part2: int = solve_part2(data)

    print(f"Day 1 - part 1: {solution_part1}")
    print(f"Day 1 - part 2: {solution_part2}")


if __name__ == '__main__':
    main()
