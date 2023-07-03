import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def dfs(node):
    visited = [False]*(n+1)
    stk = [node]
    cnt = 0
    while stk:
        now = stk.pop()
        if not visited[now]:
           visited[now] = True
           stk += graph[now]
           cnt += 1
    return cnt


max_num = 0
ans = []
for i in range(1, n+1):
    d = dfs(i)
    if d > max_num:
        max_num = d
        ans = [i]
    elif d == max_num:
        ans.append(i)
print(*ans)