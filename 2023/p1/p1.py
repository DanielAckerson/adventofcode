#! /usr/bin/env python3
"""--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

import itertools
from argparse import ArgumentParser
from collections.abc import Iterator, Sequence
from pathlib import Path

def parse_calibration_value(line: str) -> int:
    valid_digits = '1234567890'
    first_digit = next(c for c in line if c in valid_digits)
    last_digit = next(c for c in reversed(line) if c in valid_digits)

    return int(first_digit + last_digit)

digit_lexicon = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}


def find_digits(line: str, lexicon: dict[str, str]) -> Iterator[str]:
    """Find digits (first instance only) in a line using a lexicon."""

    return (digit for _i, digit in sorted(
        filter(
            lambda i: i[0] >= 0,
            ((line.find(term), lexicon[term]) for term in lexicon)),
        key=lambda i: i[0]))


def parse_calibration_value_revised(line: str) -> int:
    first_digit = next(find_digits(line, lexicon=digit_lexicon))

    # same as first_digit, except we search in reverse order. lexicon terms need to be reversed too
    last_digit = next(find_digits(line[::-1], lexicon={term[::-1]: digit for term, digit in digit_lexicon.items()}))

    return int(first_digit + last_digit)


def main():
    parser = ArgumentParser()

    parser.add_argument('path', type=Path, nargs='?', default=Path('input.txt'), help='calibration document path')

    args = parser.parse_args()
    calibration_document_path = args.path

    with calibration_document_path.open('r') as cal_doc_file:
        solution_part_one = sum(parse_calibration_value(line) for line in cal_doc_file.readlines())

        cal_doc_file.seek(0)

        solution_part_two = sum(parse_calibration_value_revised(line) for line in cal_doc_file.readlines())

    print(f'part one: {solution_part_one}')
    print(f'part two: {solution_part_two}')


if __name__ == '__main__':
    main()
