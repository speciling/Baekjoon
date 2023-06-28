import sys
input = sys.stdin.readline

n = int(input())
cost = [float('inf')]*(n+1)
visited = [False]*(n+1)
graph = {i: {} for i in range(n+1)}
for _ in range(int(input())):
    s, e, c = map(int, input().rstrip().split())
    if e in graph[s]:
        graph[s][e] = min(graph[s][e], c)
    else:
        graph[s][e] = c

start, dest = map(int, input().rstrip().split())
cost[start] = 0

for _ in range(n):
    min_val = float('inf')
    idx = 0
    for i in range(1, n+1):
        if not visited[i] and cost[i] < min_val:
            min_val = cost[i]
            idx = i

    visited[idx] = True
    for i in graph[idx]:
        cost[i] = min(cost[i], cost[idx]+graph[idx][i])

print(cost[dest])