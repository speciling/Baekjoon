import sys
input = sys.stdin.readline
n = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
stk = [1]
cnt = 0
while stk:
    now = stk.pop()
    if not visited[now]:
        visited[now] = True
        stk += graph[now]
        cnt += 1
print(cnt-1)