from src.day2 import solve_part2, parse_data, solve_part1
from src.file_utils import read_data


class TestDay2:

    def test_part1_valid_base(self):
        data = parse_data(RAW)
        solution = solve_part1(data)
        assert solution == 150

    def test_part2_valid_base(self):
        data = parse_data(RAW)
        solution = solve_part2(data)
        assert solution == 900

    def test_part1_valid_solution(self):
        data = parse_data(read_data('day2.txt'))
        solution = solve_part1(data)
        assert solution == 2117664

    def test_part2_valid_solution(self):
        data = parse_data(read_data('day2.txt'))
        solution = solve_part2(data)
        assert solution == 2073416724


RAW = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

