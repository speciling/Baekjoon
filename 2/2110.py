import sys
n, c = map(int, input().split())
houses = sorted(map(int, sys.stdin.readlines()))
s, e, ans = 1, (houses[-1]-houses[0])//(c-1), 0
while s <= e:
    d = (s+e)//2
    prev, cnt = houses[0], c-1
    for h in houses:
        if h-prev >= d:
            prev = h
            cnt -= 1
            if not cnt:
                break
    if cnt:
        e = d-1
    else:
        ans = d
        s = d+1
print(ans)