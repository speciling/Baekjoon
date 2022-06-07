from sys import stdin
from collections import deque

m, n = map(int, input().split())
box = [list(map(int, stdin.readline().split())) for _ in range(n)]
que = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            que.append([0, i, j])

elapsed_time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que:
    time, x, y = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                que.append([time+1, nx, ny])
                if elapsed_time < time+1:
                    elapsed_time = time+1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            elapsed_time = -1
            break
print(elapsed_time)