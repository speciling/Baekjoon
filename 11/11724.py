from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
visited = [False] * (n+1)
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)


def bfs(graph, v, visited):
    if not visited[v]:
        queue = deque([v])
        visited[v] = True
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return 1
    else:
        return 0


cnt = 0
for i in range(1, n+1):
    cnt += bfs(edges, i, visited)
print(cnt)