from sys import stdin

chess = []
for _ in range(4):
    chess += [list('BWBWBWBW')]+[list('WBWBWBWB')]

N, M = map(int, stdin.readline().split())

board = []
for _ in range(N):
    board += [list(stdin.readline().strip())]

ans = set()

for i in range(M-7):
    for j in range(N-7):
        change = 0
        for k in range(8):
            for l in range(8):
                if chess[k][l] == board[j+k][i+l]:
                    change += 1
        ans.add(change)
        ans.add(64-change)

print(min(ans))