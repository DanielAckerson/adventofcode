#! /usr/bin/env python3

import re
from argparse import ArgumentParser
from collections.abc import Iterator
from pathlib import Path

def load_schematic(path: Path) -> tuple[dict, dict]:
    symbols = dict[tuple[int, int], re.Match]()
    numbers = dict[tuple[int, int], re.Match]()
    y = 0

    with path.open('r') as eng_file:
        for line in eng_file.readlines():
            for sym in re.finditer('[-+#$%&*/=@]', line):
                symbols[(sym.span()[0], y)] = sym

            for num in re.finditer('\d+', line):
                numbers[(num.span()[0], y)] = num

            y += 1

    return symbols, numbers


def iter_neighbors(posx: int, posy: int) -> Iterator[tuple[int, int]]:
    for y in range(posy - 1, posy + 2):
        for x in range(posx - 1, posx + 2):
            if posx == x and posy == y:
                continue
            yield x, y


def has_symbol_neighbor(posx: int, posy: int, symbols: dict[tuple[int, int], re.Match]) -> bool:
    for nx, ny in iter_neighbors(posx, posy):
        if symbols.get((nx, ny), None):
            return True
    return False


def iter_part_numbers(symbols: dict[tuple[int, int], re.Match], numbers: dict[tuple[int, int], re.Match]) -> Iterator[int]:
    for (_, y), num in numbers.items():
        for x in range(*num.span()):
            if has_symbol_neighbor(x, y, symbols):
                yield int(num[0])
                break


def solution_part_one(path: Path) -> int:
    symbols, numbers = load_schematic(path)
    return sum(iter_part_numbers(symbols, numbers))


def main():
    parser = ArgumentParser()

    parser.add_argument('path', type=Path, nargs='?', default=Path('input.txt'), help='engine schematic path')

    args = parser.parse_args()
    engine_schematic_path = args.path

    print(f'solution 1: {solution_part_one(engine_schematic_path)}')


if __name__ == '__main__':
    main()
