from sys import stdin

n = int(stdin.readline())
infected = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, infected)
print(infected.count(1)-1)