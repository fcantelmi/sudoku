import os
import re


class Sudoku:

    def __init__(self, values):
        self.values = values

    def __str__(self):
        sudoku = ""

        for row_index in range(9):
            split = ["." if it is None else str(it) for it in self.get_row(row_index)]
            sudoku += " ".join(split)
            sudoku += os.linesep

        return sudoku

    def set_value(self, row, col, value):
        self.values[row * 9 + col] = value

    def get_value(self, row, col):
        return self.values[row * 9 + col]

    def get_box(self, row, col):
        box_row = (row // 3) * 3  # returns 0, 3, or 6
        box_col = (col // 3) * 3  # returns 0, 3, or 6

        return [self.get_value(box_row + it_row, box_col + it_col) for it_row in range(3) for it_col in range(3)]

    def get_row(self, row):
        index = 9 * row
        return self.values[index:index + 9]

    def get_col(self, col):
        return self.values[col::9]

    def possible(self, row, col, value):
        if value in self.get_row(row):
            return False

        if value in self.get_col(col):
            return False

        if value in self.get_box(row, col):
            return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.get_value(row, col) is None:
                    for value in range(1, 10):
                        if self.possible(row, col, value):
                            self.set_value(row, col, value)
                            if self.solve() is False:
                                self.set_value(row, col, None)
                    return False

        print(self)
        return True

    @classmethod
    def parse(cls, sudoku):
        no_whitespace = re.sub(r"\s+", "", sudoku)
        values = [int(val) if val in '123456789' else None for val in no_whitespace]
        return cls(values)


unsolved = '.......15.49......2..3.17..8..2...9..9.....7..7...6..1..49.5..7......54.61.......'
# expected = '738629415149578632256341789861257394592413876473896251324985167987162543615734928'
expected = """
    9  2  1  6  5  8  7  4  3
    8  3  4  7  1  2  5  6  9
    6  5  7  4  9  3  1  2  8
    4  6  8  2  7  9  3  1  5
    1  9  5  8  3  6  4  7  2
    2  7  3  5  4  1  8  9  6
    3  8  2  1  6  4  9  5  7
    5  1  6  9  8  7  2  3  4
    7  4  9  3  2  5  6  8  1
"""
android = """
            .  .  .  .  1  3  .  .  .
            .  .  .  6  8  .  .  .  2
            .  .  6  .  .  .  .  .  .
            2  .  .  4  7  .  .  .  5
            4  .  .  .  .  8  .  .  .
            .  .  5  .  6  .  .  3  .
            .  .  .  3  .  5  .  2  6
            .  .  3  .  .  .  8  .  1
            .  .  .  .  .  .  4  .  .
            """

puzzle = Sudoku.parse(unsolved)
print(puzzle)
puzzle.solve()
