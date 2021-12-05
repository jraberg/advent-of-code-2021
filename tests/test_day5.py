from src.day5 import solve_part2, solve_part1
from src.file_utils import read_data


class TestDay5:

    def test_part1_valid_base(self):
        solution = solve_part1(RAW)
        assert solution == 5

    def test_part2_valid_base(self):
        solution = solve_part2(RAW)
        assert solution == 12

    def test_part1_valid_solution(self):
        data = read_data('day5.txt')
        solution = solve_part1(data)
        assert solution == 6007

    def test_part2_valid_solution(self):
        data = read_data('day5.txt')
        solution = solve_part2(data)
        assert solution == 19349


RAW = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
