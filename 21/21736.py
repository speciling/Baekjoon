import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
graph = [list(input().rstrip()) for _ in range(n)]


def find():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'I':
                visited[i][j] = 1
                return [i, j]


def dfs():
    cnt = 0
    stk = [find()]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while stk:
        x, y = stk.pop()
        for i in move:
            nx, ny = x+i[0], y+i[1]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != 'X':
                stk.append([nx, ny])
                visited[nx][ny] = 1
                if graph[nx][ny] == 'P':
                    cnt += 1
    return cnt


print(dfs() or "TT")