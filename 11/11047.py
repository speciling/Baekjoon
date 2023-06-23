n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
cnt = 0
for i in a[::-1]:
    if k >= i:
        cnt += k//i
        k %= i
print(cnt)