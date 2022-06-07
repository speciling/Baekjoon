from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        field[y][x] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    for y in range(n):
        for x in range(m):
            if field[y][x] == 1:
                que = deque()
                que.append((x, y))
                field[y][x] = 0
                count += 1
                while que:
                    now_x, now_y = que.popleft()
                    for i in range(4):
                        new_x, new_y = now_x+dx[i], now_y+dy[i]
                        if 0 <= new_x < m and 0 <= new_y < n:
                            if field[new_y][new_x] == 1:
                                que.append((new_x, new_y))
                                field[new_y][new_x] = 0
    print(count)

