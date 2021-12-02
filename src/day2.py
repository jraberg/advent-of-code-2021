from dataclasses import dataclass
from typing import List, NamedTuple

from src.file_utils import read_data


class Command(NamedTuple):
    command: str
    units: int

    @staticmethod
    def parse(command: str):
        cmd, u = command.split(' ')
        return Command(command=cmd, units=int(u))


@dataclass
class Submarine:
    forward: int = 0
    depth: int = 0
    aim: int = 0

    def move(self, cmd: Command):
        if cmd.command == 'down':
            self.depth += cmd.units
        elif cmd.command == 'up':
            self.depth -= cmd.units
        elif cmd.command == 'forward':
            self.forward += cmd.units

    def execute_commands(self, cmds: List[Command]):
        for cmd in cmds:
            self.move(cmd)


@dataclass
class Submarine2(Submarine):
    aim: int = 0

    def move(self, cmd: Command):
        if cmd.command == 'down':
            self.aim += cmd.units
        elif cmd.command == 'up':
            self.aim -= cmd.units
        elif cmd.command == 'forward':
            self.forward += cmd.units
            self.depth = self.depth + self.aim * cmd.units

    def execute_commands(self, cmds: List[Command]):
        for cmd in cmds:
            self.move(cmd)


def solve_part1(data: List[Command]) -> int:
    sub = Submarine()
    sub.execute_commands(data)
    return sub.forward * sub.depth


def solve_part2(data):
    sub = Submarine2()
    sub.execute_commands(data)
    return sub.forward * sub.depth


def parse_data(raw: str) -> List[Command]:
    return [Command.parse(cmd) for cmd in raw.split('\n')]


def main():
    raw = read_data("day2.txt")
    data = parse_data(raw)
    solution_part1: int = solve_part1(data)
    solution_part2: int = solve_part2(data)

    print(f"Day 2 -> part 1: {solution_part1}")
    print(f"Day 2 -> part 2: {solution_part2}")


if __name__ == '__main__':
    main()
