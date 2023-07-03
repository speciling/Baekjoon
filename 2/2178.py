import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny]=='1' and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

print(visited[n-1][m-1])