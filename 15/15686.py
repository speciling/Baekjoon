from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().rstrip().split() for _ in range(n)]
houses = []
stores = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == '1':
            houses.append((r, c))
        elif graph[r][c] == '2':
            stores.append((r, c))

ans = float("inf")
for comb in combinations(stores, m):
    dist = [float("inf")]*len(houses)
    for r, c in comb:
        for idx, h in enumerate(houses):
            dist[idx] = min(dist[idx], abs(h[0]-r)+abs(h[1]-c))
    ans = min(ans, sum(dist))
print(ans)