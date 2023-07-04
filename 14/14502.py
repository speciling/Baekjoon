import sys
from itertools import combinations
input = sys.stdin.readline
move = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(graph, nodes):
    cnt = 0
    stk = nodes
    while stk:
        x, y = stk.pop()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if not graph[nx][ny]:
                graph[nx][ny] = 2
                cnt += 1
                stk.append((nx, ny))
    return cnt


n, m = map(int, input().split())
graph = [[1]*(m+2)] + [[1] + list(map(int, input().rstrip().split())) + [1] for _ in range(n)] + [[1]*(m+2)]
ans = -3
virus = []
zeros = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            zeros.append((i, j))
            ans += 1
counts = []
for i in combinations(zeros, 3):
    ngraph = [i[:] for i in graph]
    for x, y in i:
        ngraph[x][y] = 1
    counts.append(dfs(ngraph, virus[:]))

print(ans-min(counts))