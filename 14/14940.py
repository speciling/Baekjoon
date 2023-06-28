import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            ans[i][j] = 0
            if graph[i][j] == 2:
                q.append((i,j))

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] and ans[nx][ny] == -1:
            q.append((nx, ny))
            ans[nx][ny] = ans[x][y] + 1

[print(*a) for a in ans]