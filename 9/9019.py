from sys import stdin
from collections import deque


def order(o, s):
    if o == 'D':
        return (s * 2) % 10000
    elif o == 'S':
        return s - 1 if s > 0 else 9999
    elif o == 'L':
        return (s * 10) % 10000 + s//1000
    elif o == 'R':
        return s // 10 + (s % 10) * 1000


def bfs(a, b):
    d = ('D', 'S', 'L', 'R')
    route = ['' for _ in range(10000)]
    stack = deque([a])
    while stack:
        n = stack.popleft()
        for i in range(4):
            x = order(d[i], n)
            if not route[x] and x != a:
                route[x] = route[n] + d[i]
                stack.append(x)
            if x == b:
                return route[x]


for _ in range(int(input())):
    A, B = map(int, stdin.readline().split())
    print(bfs(A, B))