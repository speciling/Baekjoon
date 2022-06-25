from sys import stdin
from collections import deque
input = stdin.readline


def dfs(graph, n, visited):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if visited[i] == False:
            dfs(graph, i, visited)


def bfs(graph, n, visited):
    queue = deque([n])
    visited[n] = True
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(sorted, graph))
visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)