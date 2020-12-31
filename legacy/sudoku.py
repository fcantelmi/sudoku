class UnknownValueException:
    def __repr__(self):
        return "cell value is unknown"


class ConstraintViolationException:
    def __repr__(self):
        return "a sudoku constraint has been violated"


class Cell:
    def __init__(self, known_value):

        if known_value.isdigit() and int(known_value) is not 0:
            self.pencil_marks = [int(known_value)]
        else:
            self.pencil_marks = [x for x in range(1, 10)]

    def __str__(self):
        return "%6s " % repr(self)

    def __repr__(self):
        marks = ""

        for mark in self.pencil_marks:
            marks += str(mark)

        return marks

    def has_known_value(self):
        # return True if len(self.pencil_marks) is 1 else False
        if len(self.pencil_marks) == 1:
            return True
        else:
            return False

    def has_pair(self):
        if len(self.pencil_marks) == 2:
            return True
        else:
            return False

    def has_triple(self):
        if len(self.pencil_marks) == 2 or len(self.pencil_marks) == 3:
            return True
        else:
            return False

    def has_value(self, value):
        found = [x for x in self.pencil_marks if x == value]
        # return True if len(found) is 1 else False
        if len(found) == 1:
            return True
        else:
            return False

    def get_known_value(self):
        if self.has_known_value() is False:
            raise UnknownValueException()

        return self.pencil_marks[0]

    def get_values(self):
        return self.pencil_marks

    def set_known_value(self, known_value):
        self.pencil_marks = [int(known_value)]

    def remove_value(self, value):
        if self.has_known_value() is False:
            for mark in self.pencil_marks:
                if mark == value:
                    self.pencil_marks.remove(value)
                    break


def find_hidden_pairs(cells):
    # determine the digits that only appear twice
    twice_only = []
    for digit in range(1, 10):
        found = [cell for cell in cells if cell.has_value(digit)]
        if len(found) == 2:
            twice_only.append(digit)

    if len(twice_only) > 0:
        for i in range(0, len(twice_only)):
            for j in range(i + 1, len(twice_only)):
                digit1 = twice_only[i]
                digit2 = twice_only[j]

                # create a list of potential pair cells (skip known pairs)
                pair_cells = [cell for cell in cells if
                              not cell.has_pair() and cell.has_value(digit1) and cell.has_value(digit2)]

                # only remove values if we find two cells.  the avoids the
                # case where there are three unknown values spread over
                # three cells in a "12", "23", "31" fashion.
                if len(pair_cells) == 2:
                    for pair_cell in pair_cells:
                        for digit in range(1, 10):
                            if digit != digit1 and digit != digit2:
                                pair_cell.remove_value(digit)


def find_hidden_triples(cells):
    triples = [cell for cell in cells if cell.has_triple()]
    print(triples)


class Grid:
    def __init__(self, grid):
        self.cells = [Cell(val) for val in grid if val in '0.-123456789']

    def __str__(self):
        grid_str = ""

        for row in range(9):
            for cell in self.get_row(row):
                grid_str += str(cell)
            grid_str += "\n"

        return grid_str

    def is_solved(self):
        # return True if self.get_known_value_count() == 81 else False
        if self.get_known_value_count() is 81:
            return True
        else:
            return False

    def get_known_value_count(self):
        count = 0

        for cell in self.cells:
            if cell.has_known_value():
                count += 1

        return count

    def get_row_index(self, row):
        return 9 * row

    def get_row(self, number):
        index = self.get_row_index(number)
        return self.cells[index:index + 9]

    def get_col(self, number):
        return self.cells[number::9]

    def get_minigrid(self, row, col):
        cells = []

        for mg_row in range(3 * row, 3 * row + 3):
            cells.extend(self.get_row(mg_row)[3 * col:3 * col + 3])

        return cells

    def enforce_cells_constraints_pairs(self, cells):
        # check for pairs.  if the same pair of digits appears in
        # two cells then these two digits may be removed from the
        # other cells even if the values are not known yet
        pairs = [cell for cell in cells if cell.has_pair() is True]
        if len(pairs) >= 2:
            for i in range(0, len(pairs)):
                pair = pairs[i]
                for j in range(i + 1, len(pairs)):
                    if repr(pair) == repr(pairs[j]):
                        # found a repeated pair.  remove these values from 
                        # unknown, non-pair cells
                        for cell in cells:
                            if not cell.has_known_value() and not cell.has_pair():
                                cell.remove_value(pair.get_values()[0])
                                cell.remove_value(pair.get_values()[1])

    def enforce_cells_constraints(self, cells):
        # check for repeated digits
        known_values = [cell.get_known_value() for cell in cells if cell.has_known_value()]
        for digit in range(1, 10):
            if known_values.count(digit) > 1:
                raise ConstraintViolationException()

        # if any cell has a known value then this value can be removed
        # as a possible value for other cells
        for cell in cells:
            if cell.has_known_value():
                for c in cells:
                    c.remove_value(cell.get_known_value())

        # if a given digit is only allowed in one of the cells it
        # must be in that cell
        for digit in range(1, 10):
            found = [cell for cell in cells if cell.has_value(digit)]
            if len(found) == 1:
                found[0].set_known_value(digit)

        find_hidden_pairs(cells)
        self.enforce_cells_constraints_pairs(cells)

    def enforce_row_constraints(self):
        for row in range(9):
            cells = self.get_row(row)
            self.enforce_cells_constraints(cells)

    def enforce_col_constraints(self):
        for col in range(9):
            cells = self.get_col(col)
            self.enforce_cells_constraints(cells)

    def enforce_minigrid_constraints(self):
        for row in range(3):
            for col in range(3):
                self.enforce_cells_constraints(self.get_minigrid(row, col))

    def enforce_constraints(self):
        prev = 0
        curr = self.get_known_value_count()

        while curr > prev:
            self.enforce_minigrid_constraints()
            self.enforce_col_constraints()
            self.enforce_row_constraints()

            prev = curr
            curr = self.get_known_value_count()

    def guess(self, cell):
        legal = True
        for value in cell.get_values():
            pre_guess = self.cells[:]
            cell.set_known_value(value)
            try:
                self.enforce_constraints()
            except ConstraintViolationException:
                print("no luck...keep guessing")
                self.cells = pre_guess
            else:
                print("found a solution.  hurray!")

    def solve(self):
        self.enforce_constraints()


#        while not self.is_solved():
#            print "guessing required!"
#            for unknown_count in range(2,10):
#                unknown_cells = [cell for cell in self.cells if len(cell.get_values()) == unknown_count]
#                for cell in unknown_cells:
#                    self.guess(cell)

grid = """
243856197
968714325
751392468
815679234
637428519
429531786
592167843
386245971
174983652
"""

grid_unsolved = """
.43....9.
...71.32.
..13.246.
8..67...4
.37...51.
4...31..6
.921.78..
.86.45...
.7....65.
"""

black_belt_7_original = """
13.....5.
2...36..9
...5..2..
.27....15
3.9.2..6.
56..8....
....4...1
.82..9..7
......9..
"""

black_belt_7 = """
13.....5.
2...36..9
...5..2..
8276..315
319.2..6.
56..8....
....4...1
.82..9..7
......9..
"""

black_belt_8_original = """
..9.827..
.........
..5.362..
52.....78
9......4.
.8.2....1
..4...1..
...823...
.7..15..9
"""

black_belt_8 = """
..91827..
.........
..5.362..
52.....78
9......4.
.8.2....1
..4...1..
1..823...
.7..15..9
"""

if __name__ == '__main__':
    g = Grid(grid)
    print(g)
    #    print g.get_minigrid(0, 0)
    #    print g.get_minigrid(0, 2)
    #    print g.get_minigrid(2, 0)
    #    print g.get_minigrid(1, 1)
    #    print g.get_minigrid(2, 2)

    gu = Grid(grid_unsolved)
    gu.solve()
    print(gu)

    bb7 = Grid(black_belt_7_original)
    bb7.solve()
    print(bb7)

    bb7 = Grid(black_belt_7)
    bb7.solve()
    print(bb7)

    bb8 = Grid(black_belt_8)
    bb8.solve()
    print(bb8)
