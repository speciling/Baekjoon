from sys import stdin


def dfs(graph, x, y):
    stack = [(x, y)]
    graph[x][y] = '0'
    cnt = 1
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1':
                stack.append((nx, ny))
                graph[nx][ny] = '0'
                cnt += 1
    return cnt


n = int(stdin.readline())
gets = [list(stdin.readline().strip()) for _ in range(n)]
nums = 0
houses = []
for i in range(n):
    for j in range(n):
        if gets[i][j] == '1':
            nums += 1
            houses.append(dfs(gets, i, j))
print(nums)
print('\n'.join(map(str, sorted(houses))))