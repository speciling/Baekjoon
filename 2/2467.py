import sys

input()
arr = list(map(int, sys.stdin.readline().rstrip().split()))
p1, p2 = 0, len(arr)-1

minN = float('inf')
ans = []
while p1 != p2:
    a, b = arr[p1], arr[p2]
    if (s:=abs(a+b)) < minN:
        minN = s
        ans = [a, b]
    if a+b < 0:
        p1 += 1
    else:
        p2 -= 1

print(*ans)