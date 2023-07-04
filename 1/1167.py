import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    s, *v, _ = map(int, sys.stdin.readline().rstrip().split())
    for i in range(0, len(v), 2):
        graph[s].append(v[i:i+2])


def dfs(graph, s, n):
    dist = [0]*(n+1)
    dist[s] = 1
    stk = [s]
    while stk:
        now = stk.pop()
        for node, d in graph[now]:
            if not dist[node]:
                stk.append(node)
                dist[node] += dist[now] + d
    return dist


dist = dfs(graph, 1, n)
print(max(dfs(graph, dist.index(max(dist)), n))-1)