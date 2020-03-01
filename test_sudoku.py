import unittest
import sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        unsolved_puzzle = """
        .  .  .  .  .  .  .  1  5
        .  4  9  .  .  .  .  .  .
        2  .  .  3  .  1  7  .  .
        8  .  .  2  .  .  .  9  .
        .  9  .  .  .  .  .  7  .
        .  7  .  .  .  6  .  .  1
        .  .  4  9  .  5  .  .  7
        .  .  .  .  .  .  5  4  .
        6  1  .  .  .  .  .  .  .
        """

        self.unsolved_puzzle = sudoku.Puzzle.parse(unsolved_puzzle)

        solved_puzzle = """
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

        self.solved_puzzle = sudoku.Puzzle.parse(solved_puzzle)
        self.all_values = frozenset(range(1, 10))

    def test_puzzle_row_values_solved(self):
        for row in range(9):
            row_values = self.solved_puzzle.row_values(row)
            self.assertEqual(self.all_values, row_values)

    def test_puzzle_col_values_solved(self):
        for col in range(9):
            col_values = self.solved_puzzle.col_values(col)
            self.assertEqual(self.all_values, col_values)

    def test_puzzle_box_values_solved(self):
        for row in range(9):
            for col in range(9):
                box_values = self.solved_puzzle.box_values(row, col)
                self.assertEqual(self.all_values, box_values)

    def test_puzzle_row_values_unsolved(self):
        values = self.unsolved_puzzle.row_values(row=0)
        self.assertEqual(frozenset({1, 5, None}), values)
        values = self.unsolved_puzzle.row_values(row=1)
        self.assertEqual(frozenset({4, 9, None}), values)

    def test_puzzle_col_values_unsolved(self):
        values = self.unsolved_puzzle.col_values(col=0)
        self.assertEqual(frozenset({2, 6, 8, None}), values)
        values = self.unsolved_puzzle.col_values(col=1)
        self.assertEqual(frozenset({1, 4, 7, 9, None}), values)


if __name__ == '__main__':
    unittest.main()
