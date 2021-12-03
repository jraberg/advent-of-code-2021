from src.day3 import solve_part2, solve_part1
from src.file_utils import read_data


class TestDay3:

    def test_part1_valid_base(self):
        solution = solve_part1(RAW)
        assert solution == 198

    def test_part2_valid_base(self):
        solution = solve_part2(RAW)
        assert solution == 230

    def test_part1_valid_solution(self):
        data = read_data('day3.txt')
        solution = solve_part1(data)
        assert solution == 3895776

    def test_part2_valid_solution(self):
        data = read_data('day3.txt')
        solution = solve_part2(data)
        assert solution == 7928162


RAW = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
