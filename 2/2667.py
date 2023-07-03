import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1))
cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            c = 1
            stk = [(i, j)]
            graph[i][j] = 0
            while stk:
                x, y = stk.pop()
                for dx, dy in move:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
                        c += 1
                        stk.append((nx, ny))
                        graph[nx][ny] = 0
            cnt.append(c)

print(len(cnt))
print('\n'.join(map(str, sorted(cnt))))