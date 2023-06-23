import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x:(x[1],x[0]))
t, cnt = 0, 0
for i in arr:
    if i[0] >= t:
        cnt += 1
        t = i[1]
print(cnt)