from sys import stdin


def check_sudoku(paper):
    nums = set(range(1, 10))
    for i in range(9):
        if set(paper[i]) != nums:
            return False
    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(paper[j][i])
        if temp != nums:
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            temp = set()
            for k in range(3):
                temp |= set(paper[j+k][i:i+3])
            if temp != nums:
                return False
    return True


tc = int(stdin.readline())
arr = [list(map(int, input().split())) for _ in range(9)]
if check_sudoku(arr):
    print('Case 1: CORRECT')
else:
    print('Case 1: INCORRECT')
for i in range(2, tc+1):
    stdin.readline()
    arr = [list(map(int, input().split())) for _ in range(9)]
    if check_sudoku(arr):
        print(f'Case {i}: CORRECT')
    else:
        print(f'Case {i}: INCORRECT')