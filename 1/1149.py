from sys import stdin
input = stdin.readline

n = int(input())
dp = [[0]*n for _ in range(3)]
dp[0][0], dp[1][0], dp[2][0] = map(int, input().split())

for i in range(1, n):
    r, g, b = map(int, input().split())
    dp[0][i] = min(dp[1][i-1], dp[2][i-1])+r
    dp[1][i] = min(dp[0][i-1], dp[2][i-1])+g
    dp[2][i] = min(dp[0][i-1], dp[1][i-1])+b

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))