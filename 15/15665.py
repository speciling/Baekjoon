from sys import stdin
from itertools import product
input = stdin.readline

n, m = map(int, input().split())
for i in sorted(list(set(product(map(int, input().split()), repeat=m)))):
    print(*i)