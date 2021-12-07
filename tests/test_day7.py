from src.day7 import solve_part2, solve_part1
from src.file_utils import read_data


class TestDay7:

    def test_part1_valid_base(self):
        solution = solve_part1(RAW)
        assert solution == 37

    def test_part2_valid_base(self):
        solution = solve_part2(RAW)
        assert solution == 168

    def test_part1_valid_solution(self):
        data = read_data('day7.txt')
        solution = solve_part1(data)
        assert solution == 331067

    def test_part2_valid_solution(self):
        data = read_data('day7.txt')
        solution = solve_part2(data)
        assert solution == 92881128


RAW = """16,1,2,0,4,2,7,1,2,14"""
