from copy import deepcopy
from time import time

color = (
    ('3;30;42', '3;30;43', '3;30;44', '3;30;45', '3;30;46'),
    ('3;31;42', '3;31;43', '3;31;44', '3;31;45', '3;31;46')
)

region = (
    (1, 1, 1, 1, 2, 2, 2, 2, 2),
    (1, 1, 1, 1, 2, 2, 4, 4, 2),
    (1, 3, 3, 5, 2, 4, 4, 4, 4),
    (3, 3, 3, 5, 4, 4, 6, 6, 6),
    (3, 3, 3, 5, 4, 6, 6, 6, 9),
    (7, 3, 5, 5, 5, 8, 6, 9, 9),
    (7, 7, 7, 5, 8, 8, 6, 6, 9),
    (7, 7, 5, 5, 8, 8, 8, 9, 9),
    (7, 7, 7, 8, 8, 8, 9, 9, 9),
)

initial_field = [
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [5, 1, 0, 0, 9, 0, 0, 6, 0],
    [0, 8, 0, 5, 0, 2, 7, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 9, 0, 0],
    [1, 4, 8, 0, 0, 0, 6, 3, 9],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
]

def print_sudoku (field):
    for y in range(9):
        for x in range(9):
            print('\x1b[%sm %s\x1b[0m' % (
                color[0][(region[y][x] - 1) % 5], field[y][x] if field[y][x] else " "), end='')
        print()

def chk_sudoku (field) -> bool:
    row_count = [[0 for x in range(9)] for y in range(9)]
    col_count = [[0 for x in range(9)] for y in range(9)]
    reg_count = [[0 for x in range(9)] for y in range(9)]
    for y in range(9):
        for x in range(9):
            if field[y][x]:
                row_count[y]                    [field[y][x] - 1] += 1
                if row_count[y]                 [field[y][x] - 1] > 1: return False
                col_count[x]                    [field[y][x] - 1] += 1
                if col_count[x]                 [field[y][x] - 1] > 1: return False
                reg_count[(region[y][x] - 1)]   [field[y][x] - 1] += 1
                if reg_count[(region[y][x] - 1)][field[y][x] - 1] > 1: return False
    return True


def solve_sudoku (field) -> bool:
    if not chk_sudoku(field):
        return False
    newfield=deepcopy(field)
    for y in range(9):
        for x in range(9):
            if not field[y][x]:
                for i in range(9):
                    newfield[y][x] = i + 1
                    if solve_sudoku(newfield):
                        return True
                return False
    print_sudoku(newfield)
    return True


if __name__ == '__main__':
    print_sudoku(initial_field)
    start = time()
    print("Solving...")
    print(solve_sudoku(initial_field))
    print(f"Time : {time() - start} seconds")
