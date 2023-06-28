import sys
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = input()

    if n>32:
        print(0)
    else:
        arr = arr.split()
        dist = 8
        for c in combinations(arr, 3):
            dist = min(dist, sum(int(c1!=c2)+(c2!=c3)+(c1!=c3) for c1,c2,c3 in zip(*c)))
            if dist == 2:
                break
        print(dist)