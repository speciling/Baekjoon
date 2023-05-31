from sys import stdin
input = stdin.readline

n = int(input())
dp = (int(input()),)
for i in range(1, n):
    line = list(map(int, input().split()))
    dp = (line[0]+dp[0], *[line[j] + max(dp[j-1],dp[j]) for j in range(1,i)], line[-1]+dp[-1])

print(max(dp))