from sys import stdin
from collections import deque


def bfs(graph, x, y, size):  # size -> 아기상어 크기, size = [크기, 잡아먹은 수]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])
    feed = []
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    sec = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n:  # n -> 공간의 크기, 공간 안에 있을 조건.
                if 0 < graph[nx][ny] < size[0] and visited[nx][ny] == 0:
                    feed.append((nx, ny))
                    sec = visited[x][y] + 1
                elif (graph[nx][ny] == 0 or graph[nx][ny] == size[0]) and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        if feed:
            while queue:  # 같은 거리에 다른 물고기 있는지 확인
                x, y = queue.popleft()
                if visited[x][y] == sec - 1:
                    for i in range(4):
                        nx, ny = x + d[i][0], y + d[i][1]
                        if 0 <= nx < n and 0 <= ny < n:  # n -> 공간의 크기, 공간 안에 있을 조건.
                            if 0 < graph[nx][ny] < size[0] and visited[nx][ny] == 0:
                                feed.append((nx, ny))
            x, y = sorted(feed)[0]
            graph[x][y] = 0
            size[1] += 1
            if size[0] == size[1]:
                size[0] += 1
                size[1] = 0
            queue = deque([(x, y)])
            feed = []
            visited = [[0] * n for _ in range(n)]
            visited[x][y] = sec
    return sec - 1 if sec > 0 else 0


n = int(input())
fishbowl = []
for i in range(n):
    line = stdin.readline().strip().split()
    for j in line:
        if j == '9':
            x = i
            y = line.index('9')
            break
    fishbowl.append(list(map(int, line)))
fishbowl[x][y] = 0
print(bfs(fishbowl, x, y, [2, 0]))