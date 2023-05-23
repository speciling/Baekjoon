n = int(input())
matrix = [input().split() for _ in range(n)]
for m in range(n):
    for s in range(n):
        for e in range(n):
            if matrix[s][e] == '0':
                if matrix[s][m] == '1' and matrix[m][e] == '1':
                    matrix[s][e] = '1'
for i in matrix:
    print(*i)