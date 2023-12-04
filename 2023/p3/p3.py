#! /usr/bin/env python3

import re
from argparse import ArgumentParser
from collections.abc import Iterator
from pathlib import Path


#SYMBOLS = '#$%&*+-/=@'
#NUMBERS = '0123456789'
#EMPTY = '.'
#CHARACTERS = set(SYMBOLS + NUMBERS + EMPTY)
#
#
#class EngineSchematic:
#    def __init__(self, path: Path):
#        self.path = path
#        self.schematic, self.width, self.height = self.read_schematic(path)
#
#    def get(self, x: int, y: int) -> str:
#        if x < 0 or x >= self.width or y < 0 or y >= self.height:
#            return ''
#        return self.schematic[x + y * self.width]
#
#    def iter_cells(self) -> Iterator[tuple[str, int, int]]:
#        for y in range(0, self.height):
#            for x in range(0, self.width):
#                yield self.get(x, y), x, y
#
#    def iter_neighbors(self, x: int, y: int) -> Iterator[tuple[str, int, int]]:
#        for cury in range(y - 1, y + 2):
#            for curx in range(x - 1, x + 2):
#                if curx == x and cury == y:
#                    continue
#                yield self.get(curx, cury), curx, cury
#                    
#    @classmethod
#    def read_schematic(cls, path: Path) -> tuple[str, int, int]:
#        with path.open('r') as schematic_file:
#            schematic = schematic_file.readline().strip()
#
#            if (line_len := len(schematic)) == 0:
#                raise RuntimeError('Empty schematic file')
#
#            width = line_len
#            height = 1
#
#            while line := schematic_file.readline().strip():
#                assert len(line) == width
#                schematic += line
#                height += 1
#
#            return schematic, width, height
#
#
#def is_number(cell: str) -> bool:
#    return bool(cell in NUMBERS)
#
#
#def is_symbol(cell: str) -> bool:
#    return bool(cell in SYMBOLS)
#
#
#def is_part_number(cell: str, engine_schematic: EngineSchematic, posx: int, posy: int) -> bool:
#    # if any of 8 neighbors of a cell is a symbol and if the cell is a number, then it is a part number
#    return is_number(cell) and any(c for c, _, _ in engine_schematic.iter_neighbors(posx, posy) if is_symbol(c))
#

def symbol_adjacent_to_number(num_match: re.Match, sym_match: re.Match) -> bool:
    ...


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


def solution_part_one(path: Path) -> int:
    symbols, numbers = load_schematic(path)
    return sum(iter_part_numbers(symbols, numbers))



def main():
    parser = ArgumentParser()

    parser.add_argument('path', type=Path, nargs='?', default=Path('input.txt'), help='engine schematic path')

    args = parser.parse_args()
    engine_schematic_path = args.path
    #engine = EngineSchematic(engine_schematic_path)

    #print(f'solution 1: {solution_part_one(engine)}')
    print(f'solution 1: {solution_part_one(engine_schematic_path)}')

    ## test EngineSchematic.get()
    #for y in range(engine.height):
    #    print(f'{engine.get(0, y)}')


if __name__ == '__main__':
    main()
