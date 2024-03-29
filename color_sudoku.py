from time import time
# globals
color = (
    ('3;30;42', '3;30;43', '3;30;44', '3;30;45', '3;30;46'),  # OK colors
    ('3;31;42', '3;31;43', '3;31;44', '3;31;45', '3;31;46')  # NOK colors
)

region = (
    (0, 0, 0, 0, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 1, 1, 3, 3, 1),
    (0, 2, 2, 4, 1, 3, 3, 3, 3),
    (2, 2, 2, 4, 3, 3, 5, 5, 5),
    (2, 2, 2, 4, 3, 5, 5, 5, 8),
    (6, 2, 4, 4, 4, 7, 5, 8, 8),
    (6, 6, 6, 4, 7, 7, 5, 5, 8),
    (6, 6, 4, 4, 7, 7, 7, 8, 8),
    (6, 6, 6, 7, 7, 7, 8, 8, 8),
)

field = [
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [5, 1, 0, 0, 9, 0, 0, 6, 0],
    [0, 8, 0, 5, 0, 2, 7, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 9, 0, 0],
    [1, 4, 8, 0, 0, 0, 6, 3, 9],  # should start with this line if algo was a bit smarter (more complex?)
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
]


def print_sudoku():
    for y in range(9):
        for x in range(9):
            print('\x1b[%sm %s\x1b[0m' % (
                color[0][region[y][x] % 5], field[y][x] if field[y][x] else " "), end='')
        print()


def ok_sudoku(x, y, z):
    for i in range(9):
        if field[y][i] == z or field[i][x] == z:
            return False  # same number on row or column
    reg = region[y][x]  # region of interest
    found = 0
    for y in range(9):
        for x in range(9):
            if region[y][x] == reg:
                if field[y][x] == z:
                    return False  # same number in the region
                found += 1
                if found == 9:
                    return True  # fast exit if all found
    return True


def solve_sudoku(iy):
    for y in range(iy, 9):
        for x in range(9):
            if not field[y][x]:
                for z in range(1, 10):
                    if ok_sudoku(x, y, z):
                        field[y][x] = z
                        if solve_sudoku(y):
                            return True  # fast exit when 1st solution found
                field[y][x] = 0
                return False  # dead end
    return True  # gotcha! all cells are filled


if __name__ == '__main__':
    print_sudoku()
    start = time()
    print("Solving...")
    print(solve_sudoku(0))
    print_sudoku()
    print(f"Time : {time() - start} seconds")
