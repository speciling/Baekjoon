from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
dp = [[0]*len(b) for _ in range(len(a))]
answer = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > answer:
                answer = dp[i][j]

print(answer)