import heapq
from sys import stdin
input = stdin.readline

h = []
for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(h, -n)
    else:
        print(-heapq.heappop(h) if h else 0)