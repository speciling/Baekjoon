from sys import stdin
raw = [[False] * 10 for _ in range(10)]
column = [[False] * 10 for _ in range(10)]
square = [[False] * 10 for _ in range(10)]
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]
# 각 행,열에 존재하는 숫자 체크
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            raw[i][sudoku[i][j]] = True
            column[j][sudoku[i][j]] = True
            square[i//3 * 3 + j//3][sudoku[i][j]] = True


# 백트래킹
def bt(num):
    if num == 81:
        for r in sudoku:
            print(*r)
        return True
    x, y = num // 9, num % 9
    if sudoku[x][y] != 0:
        return bt(num+1)
    else:
        for i in range(1, 10):
            if not raw[x][i] and not column[y][i] and not square[x//3 * 3 + y//3][i]:
                raw[x][i] = column[y][i] = square[x // 3 * 3 + y // 3][i] = True
                sudoku[x][y] = i
                if bt(num+1):
                    return True
                raw[x][i] = column[y][i] = square[x // 3 * 3 + y // 3][i] = False
                sudoku[x][y] = 0
    return False


bt(0)