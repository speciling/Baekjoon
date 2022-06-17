from sys import stdin

n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
b = [list(map(int, stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
for line in a:
    print(*line)