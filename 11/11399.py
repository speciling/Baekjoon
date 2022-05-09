n = int(input())
t = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    ans += t[i] * (n-i)

print(ans)