from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
matrix = [[float("inf")]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    matrix[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
for mid in range(1, n+1):
    for i in range(1, n+1):
            for j in range(1, n+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][mid]+matrix[mid][j])
print(sorted([sum(num[1:]), i+1] for i, num in enumerate(matrix[1:]))[0][1])