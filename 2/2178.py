from collections import deque


def bfs(graph, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    print(graph[-1][-1])


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
bfs(maze, 0, 0)