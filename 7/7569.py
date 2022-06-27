from sys import stdin
from collections import deque


def bfs(graph, queue):
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + d[i][0], y + d[i][1], z + d[i][2]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append((nx, ny, nz))


m, n, h = map(int, stdin.readline().split())
tomato = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((j, k, i))
bfs(tomato, queue)
ans = 0
for i in range(h):
    if ans == -1:
        break
    for j in range(n):
        if ans == -1:
            break
        for k in range(m):
            if tomato[i][j][k] == 0:
                ans = -1
                break
            elif tomato[i][j][k] > ans:
                ans = tomato[i][j][k]
print(ans-1 if ans > 0 else -1)