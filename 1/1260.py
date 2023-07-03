import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [list(sorted(i)) for i in graph]
visited = [False]*(n+1)
ans_dfs = []
ans_bfs = []

def dfs(node):
    ans_dfs.append(node)
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    visited[node] = True
    stk = [node]
    while stk:
        tmp = []
        for i in stk:
            ans_bfs.append(i)
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    tmp.append(j)
        stk = tmp


dfs(v)
visited = [False]*(n+1)
bfs(v)
print(*ans_dfs)
print(*ans_bfs)