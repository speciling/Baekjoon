import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]
dist[0][0] = 1

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
q = deque([(0, 0)])
broken_walls = deque()
while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not dist[nx][ny]:
            if graph[nx][ny]:
                broken_walls.append((nx, ny))
            else:
                q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

q = broken_walls
while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not graph[nx][ny]:
            if not dist[nx][ny] or dist[x][y]+1 < dist[nx][ny]:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(dist[-1][-1] or -1)