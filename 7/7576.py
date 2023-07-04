import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1))
q = deque()
ans, cnt = 1, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
        elif graph[i][j] == 0:
            cnt += 1

while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
            cnt -= 1
            graph[nx][ny] = ans = graph[x][y] + 1
            q.append((nx, ny))

print(ans-1 if not cnt else -1)