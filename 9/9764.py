dp = [[0]*2001 for _ in range(2001)]
nums = [int(input()) for _ in range(int(input()))]
for num in range(1, max(nums)+1):
    for i in range((num+1)//2, num+1):
        dp[num][i] = 1
    for i in range((num-1)//2, 0, -1):
        dp[num][i] = dp[num][i+1] + dp[num-i][i+1]
print('\n'.join(map(str, (dp[num][1]%100999 for num in nums))))