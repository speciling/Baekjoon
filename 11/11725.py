from sys import stdin
input = stdin.readline

n = int(input())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

parent = [0]*(n+1)
visited = [False]*(n+1)
visited[1] = True
stk = edge[1]
for i in edge[1]:
    parent[i] = 1

while stk:
    visited[(node:=stk.pop())] = True
    for i in edge[node]:
        if not visited[i]:
            stk.append(i)
            parent[i] = node

print('\n'.join(map(str, parent[2:])))