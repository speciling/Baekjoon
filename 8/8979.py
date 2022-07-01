from sys import stdin

n, k = map(int, stdin.readline().split())
country = [list(map(int, stdin.readline().split())) for _ in range(n)]
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if country[i][0] == k:
        rank = i+1
tied = 0
for c in country[rank-2::-1]:
    if country[rank-1][1:] == c[1:]:
        tied += 1
    else:
        break
print(rank - tied)
