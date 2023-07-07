import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().rstrip().split()))
s, e, ans = 0, max(trees), 0

while s<=e:
    mid = (s+e)//2
    amount = sum(map(lambda x: x-mid if x>mid else 0, trees))
    if amount >= m:
        ans = max(ans, mid)
        s = mid+1
    else:
        e = mid-1

print(ans)