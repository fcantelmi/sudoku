import re


def print_puzzle(grid):
    for row_index in range(9):
        print(get_row(grid, row_index))
    print()


def set_val(grid, row, col, value):
    grid[row * 9 + col] = int(value)


def get_val(grid, row, col):
    return grid[row * 9 + col]


def get_box(grid, row, col):
    box_row = (row // 3) * 3  # returns 0, 3, or 6
    box_col = (col // 3) * 3  # returns 0, 3, or 6

    return [get_val(grid, box_row + it_row, box_col + it_col) for it_row in range(3) for it_col in range(3)]


def get_row(grid, row):
    index = 9 * row
    return grid[index:index + 9]


def get_col(grid, col):
    return grid[col::9]


def possible(grid, row, col, value):
    if value in get_row(grid, row):
        return False

    if value in get_col(grid, col):
        return False

    if value in get_box(grid, row, col):
        return False

    return True


def solve(grid):
    for row in range(9):
        for col in range(9):
            if get_val(grid, row, col) == 0:
                for value in range(1, 10):
                    if possible(grid, row, col, value):
                        set_val(grid, row, col, value)
                        if solve(grid) is False:
                            set_val(grid, row, col, 0)
                return False
    print_puzzle(grid)
    return True


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

no_whitespace = re.sub(r"\s+", "", android.strip())
grid = [int(val) if val in '123456789' else 0 for val in no_whitespace]

solve(grid)
# print(get_box(grid, 8, 8))

# for row_index in range(9):
#     print(get_row(grid, row_index))
# #
# print()
#
# for col_index in range(9):
#     print(get_col(grid, col_index))
#
# print(get_val(grid, 0, 0))
# print(get_val(grid, 2, 7))
# print(get_val(grid, 7, 2))
# print(get_val(grid, 8, 8))
