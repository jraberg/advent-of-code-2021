from src.day6 import solve
from src.file_utils import read_data


class TestDay6:

    def test_part1_valid_base(self):
        solution = solve(RAW, 80)
        assert solution == 5934

    def test_part2_valid_base(self):
        solution = solve(RAW, 256)
        assert solution == 26984457539

    def test_part1_valid_solution(self):
        data = read_data('day6.txt')
        solution = solve(data, 80)
        assert solution == 352872

    def test_part2_valid_solution(self):
        data = read_data('day6.txt')
        solution = solve(data, 256)
        assert solution == 1604361182149


RAW = """3,4,3,1,2"""
