n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]  # 밟지 않을경우, 연속 1번째, 연속 2번째
dp[0] = [0, stairs[0], 0]
for i in range(1, n):
    dp[i] = [max(dp[i-1][1], dp[i-1][2]), dp[i-1][0] + stairs[i], dp[i-1][1] + stairs[i]]
print(max(dp[n-1][1:3]))
