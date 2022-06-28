from collections import deque

n, k = map(int, input().split())
nums = [0] * 100001


def bfs(graph, start, end):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000:
                if graph[i] == 0:
                    queue.append(i)
                    graph[i] = graph[v] + 1
                if i == end:
                    return graph[i]


print(bfs(nums, n, k) if n != k else 0)