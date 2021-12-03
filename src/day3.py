from collections import Counter
from dataclasses import dataclass
from typing import List, Any

from src.file_utils import read_data


@dataclass
class DiagnosticReport:
    diagnostic: List[str]

    @staticmethod
    def parse(raw: str):
        raw_data = [list(l.strip()) for l in raw.split('\n')]
        transpose_matrix = [list(row) for row in zip(*raw_data)]
        return DiagnosticReport([''.join(r) for r in transpose_matrix])

    def power_consumption(self):
        freq = [Counter(col).most_common()[0] for col in self.diagnostic]
        most_common_by_col = ''.join([f[0] for f in freq])
        gamma = int(most_common_by_col, base=2)
        epsilon = gamma ^ int('1' * len(most_common_by_col), base=2)
        return gamma * epsilon


@dataclass
class OxygenConsumption:
    diagnostic_report: List[str]

    @staticmethod
    def parse(raw: str):
        raw_data = [l.strip() for l in raw.split('\n')]
        return OxygenConsumption(raw_data)

    def filter1(self, report, pos: int):
        freq = dict(Counter([row[pos] for row in report]))
        most_freq_digit = '1' if freq['1'] >= freq['0'] else '0'
        return [row for row in report if row[pos] == most_freq_digit]

    def filter2(self, report, pos: int):
        freq = dict(Counter([row[pos] for row in report]))
        least_freq_digit = '1' if freq['1'] < freq['0'] else '0'
        return [row for row in report if row[pos] == least_freq_digit]

    def oxygen_rating(self):
        diag_report = self.diagnostic_report
        position = 0
        while len(diag_report) > 1:
            diag_report = self.filter1(diag_report, position)
            position = position + 1 if position < len(diag_report[0]) else 0
        return int(diag_report[0], base=2)

    def scrubber_rating(self):
        diag_report = self.diagnostic_report
        position = 0
        while (len(diag_report) > 1):
            diag_report = self.filter2(diag_report, position)
            position = position + 1 if position < len(diag_report[0]) else 0
        return int(diag_report[0], base=2)


def solve_part1(data):
    diag = DiagnosticReport.parse(data)
    return diag.power_consumption()


def solve_part2(data):
    oxygen_consumption = OxygenConsumption.parse(data)
    return oxygen_consumption.oxygen_rating() * oxygen_consumption.scrubber_rating()


def main():
    raw = read_data("day3.txt")

    solution_part1: int = solve_part1(raw)
    solution_part2: int = solve_part2(raw)

    print(f"Day 2 -> part 1: {solution_part1}")
    print(f"Day 2 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
