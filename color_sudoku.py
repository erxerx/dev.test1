from time import time

color = (
    ('3;30;42', '3;30;43', '3;30;44', '3;30;45', '3;30;46'),
    ('3;31;42', '3;31;43', '3;31;44', '3;31;45', '3;31;46')
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 1, 0, 0, 9, 0, 0, 6, 0],
    [0, 8, 0, 5, 0, 2, 7, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 9, 0, 0],
    [1, 4, 8, 0, 0, 0, 6, 3, 9],  ## should start with this line
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
]

row_count = [[0 for x in range(9)] for y in range(9)]
col_count = [[0 for x in range(9)] for y in range(9)]
reg_count = [[0 for x in range(9)] for y in range(9)]
for y in range(9):
    for x in range(9):
        if field[y][x]:
            row_count[y][field[y][x] - 1] += 1
            col_count[x][field[y][x] - 1] += 1
            reg_count[region[y][x]][field[y][x] - 1] += 1

def print_sudoku ():
    for y in range(9):
        for x in range(9):
            print('\x1b[%sm %s\x1b[0m' % (
                color[0][region[y][x] % 5], field[y][x] if field[y][x] else " "), end='')
        print()

def solve_sudoku (ix,iy,iz) -> bool:
    row_count[iy][iz - 1] += 1
    if row_count[iy][iz - 1] > 1: return False
    col_count[ix][iz - 1] += 1
    if col_count[ix][iz - 1] > 1: return False
    reg_count[region[iy][ix]][iz - 1] += 1
    if reg_count[region[iy][ix]][iz - 1] > 1: return False
    print([ row_count[x].count(0) for x in range(9) ])
    print([ col_count[x].count(0) for x in range(9) ])
    print([ reg_count[x].count(0) for x in range(9) ])
    # start with min row, col or reg
    for y in range(9):
        for x in range(9):
            if not field[y][x]:
                for z in range(1,10):
                    field[y][x] = z
                    if solve_sudoku(x,y,z):
                        return True
                field[y][x] = 0
                return False
    print_sudoku()
    return True

if __name__ == '__main__':
    print_sudoku()
    start = time()
    print("Solving...")
    print(solve_sudoku(2,0,9))
    print(f"Time : {time() - start} seconds")
