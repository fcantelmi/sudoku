import unittest
import re
import sudoku


class SudokuTest(unittest.TestCase):

    def solve_and_compare(self, unsolved, expected):
        expected = re.sub("\\s+", "", expected)

        grid = sudoku.Grid(unsolved)
        grid.solve()
        if not grid.is_solved():
            print()
            print(grid)

        self.assertTrue(grid.is_solved())
        print(grid)
        solved = re.sub("\s+", "", str(grid))

        self.assertEqual(len(expected), len(solved))
        self.assertEqual(expected, solved)

    def test_hidden_triple(self):
        # http://hodoku.sourceforge.net/en/tech_hidden.php
        unsolved = """
            2  8  .  .  .  .  4  7  3
            5  3  4  8  2  7  1  9  6
            .  7  1  .  3  4  .  8  .
            3  .  .  5  .  .  .  4  .
            .  .  .  3  4  .  .  6  .
            4  6  .  7  9  .  3  1  .
            .  9  .  2  .  3  6  5  4
            .  .  3  .  .  9  8  2  1
            .  .  .  .  8  .  9  3  7
            """
        expected = """
            2  8  .  .  .  .  4  7  3
            5  3  4  8  2  7  1  9  6
            .  7  1  .  3  4  .  8  .
            3  .  .  5  .  .  .  4  .
            .  .  .  3  4  .  .  6  .
            4  6  .  7  9  .  3  1  .
            .  9  .  2  .  3  6  5  4
            .  .  3  .  .  9  8  2  1
            .  .  .  .  8  .  9  3  7
            """
        self.solve_and_compare(unsolved, expected)

    def test_android_expert(self):
        unsolved = """
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
        expected = """
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
        self.solve_and_compare(unsolved, expected)

    def test_vorederman(self):
        unsolved = '...65.7.3...71.5.9.5....1..4.8......19......2...54..9.3.2......51......4...32..8.'
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
        self.solve_and_compare(unsolved, expected)

    def test_very_hard_272(self):
        unsolved = '..61.....14......8....48..2..93...5..6.....4..8...52..2..67....6......81.....95..'
        expected = '876192435142563978935748612429386157561927843387415269258671394693254781714839526'
        self.solve_and_compare(unsolved, expected)

    def test_very_hard_272(self):
        unsolved = '..61.....14......8....48..2..93...5..6.....4..8...52..2..67....6......81.....95..'
        expected = '876192435142563978935748612429386157561927843387415269258671394693254781714839526'
        self.solve_and_compare(unsolved, expected)

    def test_very_hard_271(self):
        unsolved = '..38.94...4..1..7..........7..1.2..4..9...1..8..3.6..2..........2..6..9...57.36..'
        expected = '163879425948215376572634819756182934239547168814396752687951243321468597495723681'
        self.solve_and_compare(unsolved, expected)

    def test_hard_169(self):
        unsolved = '..142.........92...3......8.6.2.8..32.......91..5.6.2.6......3...81.........759..'
        expected = '891427365546389271732651498467298153253714689189536724615942837978163542324875916'
        self.solve_and_compare(unsolved, expected)

    def test_hard_165(self):
        unsolved = '....7...9.6321...5.9........3........216.735........4........9.7...3216.1...8....'
        expected = '214375689863219475597468213938154726421697358675823941356741892789532164142986537'
        self.solve_and_compare(unsolved, expected)

    def test_hard_164(self):
        unsolved = '...6.1.4...5...8.3.4.5...1.8.7.....9.........5.....2.1.2...5.7.7.6...4...5.9.3...'
        expected = '289631547175249863643587912817324659392156784564798231921465378736812495458973126'
        self.solve_and_compare(unsolved, expected)

    def test_hard_163(self):
        unsolved = '......62.34...5..9..5..7..8..8......97.....31......4..2..1..5..4..3...72.19......'
        expected = '897431625342865719165927348638214957974658231521793486283176594456389172719542863'
        self.solve_and_compare(unsolved, expected)

    def test_hard_162(self):
        unsolved = '....3..8..4.7..2....5..8.9..2..1....3.4...6.8....2..5..6.9..8....9..7.3..3..6....'
        expected = '192635784843791265675248391527816943314579628986324157461953872259187436738462519'
        self.solve_and_compare(unsolved, expected)

    def test_hard_161(self):
        unsolved = '..9..4..2.5..8.4..8......3....2....9.8..4..6.7....9....9......1..6.1..2.3..4..8..'
        expected = '639574182251386497847921635163258749985147263724639518498762351576813924312495876'
        self.solve_and_compare(unsolved, expected)

    def test_easy_17(self):
        unsolved = '.......15.49......2..3.17..8..2...9..9.....7..7...6..1..49.5..7......54.61.......'
        expected = '738629415149578632256341789861257394592413876473896251324985167987162543615734928'

        self.solve_and_compare(unsolved, expected)


if __name__ == '__main__':
    unittest.main()
