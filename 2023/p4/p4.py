#! /usr/bin/env python3

import re
from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ScratchCard:
    card_id: str
    winning: list[int]
    numbers: list[int]

    def score(self) -> int:
        return 0 # TODO: impl


def parse_card_id(card_info: str) -> int:
    if m := re.match('Card (?P<card>\d+)', card_info):
        return int(m['card'])
    return -1


def parse_numbers(numbers: str) -> list[int]:
    return list(map(int, filter(bool, numbers.strip().split(' '))))


def parse_scratchcard(line: str) -> ScratchCard:
    card_info, number_info = line.split(':')
    winning, numbers = number_info.split('|')

    return ScratchCard(
        card_id=parse_card_id(card_info),
        winning=parse_numbers(winning),
        numbers=parse_numbers(numbers))


def solution_part_one(scratchcard_path: Path) -> int:
    with scratchcard_path.open('r') as input_file:
        for line in input_file.readlines():
            card = parse_scratchcard(line)
            print(card)


def main():
    parser = ArgumentParser()

    parser.add_argument('path', type=Path, nargs='?', default=Path('input.txt'), help='scratch cards path')

    args = parser.parse_args()

    print('solution, part one:', solution_part_one(args.path))


if __name__ == '__main__':
    main()
