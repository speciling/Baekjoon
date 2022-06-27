from sys import stdin


def dfs(graph, x, y):
    color = graph[x][y]
    graph[x][y] = 0
    stack = [(x, y)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == color:
                    stack.append((nx, ny))
                    graph[nx][ny] = 0


n = int(stdin.readline())
picture = [[0]*n for _ in range(n)]
picture2 = [[0]*n for _ in range(n)]
for i in range(n):
    picture[i] = list(stdin.readline().strip())
    for j in range(n):
        if picture[i][j] != 'G':
            picture2[i][j] = picture[i][j]
        else:
            picture2[i][j] = 'R'
cnt = [0,0]
for i in range(n):
    for j in range(n):
        if picture[i][j] != 0:
            cnt[0] += 1
            dfs(picture, i, j)
        if picture2[i][j] != 0:
            cnt[1] += 1
            dfs(picture2, i, j)
print(*cnt)