from math import ceil
from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b, c = map(int, stdin.readline().split())
ans = 0
for i in a:
    if b >= i:
        ans += 1
    else:
        ans += ceil((i-b)/c) + 1
print(ans)
