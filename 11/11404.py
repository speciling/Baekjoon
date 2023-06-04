from sys import stdin
input = stdin.readline

n = int(input())
matrix = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    matrix[a][b] = min(matrix[a][b], c)

for i in range(1, n+1):
    matrix[i][i] = 0

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            matrix[s][e] = min(matrix[s][e], matrix[s][k]+matrix[k][e])

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == float('inf'):
            matrix[i][j] = 0

for i in matrix[1:]:
    print(*i[1:])