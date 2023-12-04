#! /usr/bin/env python3
"""--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 538046.
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 81709807.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

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
            for sym in re.finditer('[-+#$%&\*/=@]', line):
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


def iter_number_neighbors(posx, posy, numbers) -> Iterator[tuple[int, int, re.Match]]:
    neighbor_cells = list(iter_neighbors(posx, posy))
    candidate_neighbors = filter(lambda n: posy - 1 <= n[1] <= posy + 1, numbers)

    for x, y in candidate_neighbors:
        num = numbers[(x, y)]
        startx, stopx = num.span()
        for nx, ny in neighbor_cells:
            if startx <= nx < stopx and ny == y:
                yield x, y, num
                break


def iter_gear_ratios(symbols: dict[tuple[int, int], re.Match], numbers: dict[tuple[int, int], re.Match]) -> Iterator[int]:
    # iter * symbols
        # filter by symbols with exactly 2 numbers as neighbors
            # yield the product of those 2 neighboring numbers.

    for (sx, sy), sym in symbols.items():
        if sym[0] != '*':
            continue
        neighbors = list(iter_number_neighbors(sx, sy, numbers))
        if len(neighbors) == 2:
            gears = [int(n[2].group()) for n in neighbors]
            yield gears[0] * gears[1]
        

def solution_part_two(path: Path) -> int:
    symbols, numbers = load_schematic(path)
    return sum(iter_gear_ratios(symbols, numbers))


def main():
    parser = ArgumentParser()

    parser.add_argument('path', type=Path, nargs='?', default=Path('input.txt'), help='engine schematic path')

    args = parser.parse_args()
    engine_schematic_path = args.path

    print(f'solution 1: {solution_part_one(engine_schematic_path)}')
    print(f'solution 2: {solution_part_two(engine_schematic_path)}')


if __name__ == '__main__':
    main()
