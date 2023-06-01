from sys import stdin
input = stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
dist = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = dist[b][a] = l

for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for s in range(1, n):
        for e in range(s+1, n+1):
            dist[e][s] = dist[s][e] = min(dist[s][e], dist[s][k]+dist[k][e])

res = items[:]

for i in range(1, n+1):
    for j in filter(lambda x:dist[i][x]<=m, (k for k in range(i+1,n+1))):
        res[i] += items[j]
        res[j] += items[i]

print(max(res))