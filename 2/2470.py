import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
s, e, min_v, ans = 0, n-1, float("inf"), []
while s < e:
    if abs(arr[s]+arr[e]) < min_v:
        min_v = abs(arr[s]+arr[e])
        ans = [arr[s], arr[e]]
    if arr[s]+arr[e]>0:
        e -= 1
    else:
        s += 1
print(*ans)