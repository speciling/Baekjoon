from sys import stdin
from collections import deque


def bfs(graph, n, count):
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if len(graph[v]) == 1:
            if count[graph[v][0]] == 0 or count[graph[v][0]] > count[v]:  # count[graph[v][0]]이 count[v]+1 일 수 있음
                queue.appendleft(graph[v][0])
                count[graph[v][0]] = count[v]
        else:
            for i in graph[v]:
                if i <= 100 and count[i] == 0:
                    queue.append(i)
                    count[i] = count[v] + 1


route = [[]]+[[i+j for j in range(1, 7)] for i in range(1, 101)]
for _ in range(sum(map(int, stdin.readline().split()))):
    x, y = map(int, stdin.readline().split())
    route[x] = [y]
min_roll = [0] * 101
bfs(route, 1, min_roll)
print(min_roll[100])