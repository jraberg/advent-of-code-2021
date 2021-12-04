import re
from dataclasses import dataclass
from typing import List

from src.file_utils import read_data


def flatten(matrix: List[List[int]]):
    return [value for row in matrix for value in row]


@dataclass
class Board:
    board: List[List[int]]
    h_matches: List[List[int]]
    v_matches: List[List[int]]
    bingo = False
    score = 0

    def play(self, num: int):
        self.check_rows(num)
        self.check_cols(num)
        return self.is_bingo()

    @staticmethod
    def parse(raw: str):
        board = [[int(v) for v in re.split(r'\W+', line) if v] for line in raw.split('\n')]
        return Board(board, [[], [], [], [], []], [[], [], [], [], []])

    def check_rows(self, num):
        for i, row in enumerate(self.board):
            if num in row:
                self.h_matches[i].append(num)

    def check_cols(self, num):
        for i in range(len(self.board)):
            for board_num in [row[i] for row in self.board]:
                if num == board_num:
                    self.v_matches[i].append(num)

    def is_bingo(self):
        bingo_rows = [len(row) == 5 for row in self.h_matches]
        bingo_cols = [len(col) == 5 for col in self.v_matches]
        self.bingo = any(bingo_rows + bingo_cols)
        return self.bingo

    def get_unmarked_numbers(self):
        board_numbers = flatten(self.board)
        marked_numbers = list(set(flatten(self.v_matches) + flatten(self.h_matches)))
        return [d for d in board_numbers if d not in marked_numbers]

    def set_final_score(self, num: int):
        self.score = sum(self.get_unmarked_numbers()) * num


@dataclass
class Bingo:
    boards: List[Board]

    @staticmethod
    def parse(raw: List[str]):
        boards = [Board.parse(b) for b in raw]
        return Bingo(boards)

    def play(self, nums: List[int]):
        for num in nums:
            for board in [b for b in self.boards if not b.bingo]:
                has_bingo = board.play(num)
                if has_bingo:
                    board.set_final_score(num)
                    yield board


def parse(raw: str) -> [str, List[str]]:
    parts = [p for p in raw.split('\n\n')]
    nums = [int(n) for n in parts[0].split(',')]
    raw_boards = parts[1:]
    return nums, raw_boards


def solve_part1(raw: str):
    numbers, data = parse(raw)
    bingo = Bingo.parse(data)
    return next(bingo.play(numbers)).score


def solve_part2(raw: str):
    numbers, data = parse(raw)
    bingo = Bingo.parse(data)
    bingo_boards = [b for b in bingo.play(numbers)]
    return bingo_boards[-1].score


def main():
    raw = read_data("day4.txt")

    solution_part1: int = solve_part1(raw)
    solution_part2: int = solve_part2(raw)

    print(f"Day 2 -> part 1: {solution_part1}")
    print(f"Day 2 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
