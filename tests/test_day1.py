from src.day1 import solve_part1, solve_part2, parse_data
from src.file_utils import read_data


class TestDay1:
    def test_part1_valid_solution(self):
        data = parse_data(read_data('day1.txt'))
        solution = solve_part1(data)
        assert solution == 1292

    def test_part1_valid_base(self):
        data = parse_data(RAW)
        solution = solve_part1(data)
        assert solution == 7

    def test_part2_valid_solution(self):
        data = parse_data(read_data('day1.txt'))
        solution = solve_part2(data)
        assert solution == 1262

    def test_part2_valid_base(self):
        data = parse_data(RAW)
        solution = solve_part2(data)
        assert solution == 5


RAW = """199
200
208
210
200
207
240
269
260
263"""

