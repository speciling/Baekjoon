import sys

k, n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readlines()))
s, e, ans = 1, max(arr), -1
while s<=e:
    m = (s+e)//2
    num = sum(i//m for i in arr)
    if num >= n:
        ans = m
        s = m+1
    else:
        e = m-1
print(ans)