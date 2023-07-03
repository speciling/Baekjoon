from sys import stdin
input = stdin.readline

n = int(input())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

parent = [0]*(n+1)
parent[1] = -1
stk = edge[1]
for i in edge[1]:
    parent[i] = 1

while stk:
    for i in edge[node:=stk.pop()]:
        if not parent[i]:
            stk.append(i)
            parent[i] = node

print('\n'.join(map(str, parent[2:])))