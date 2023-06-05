dp = [float('inf')]*100001
n, k = map(int, input().split())
dp[n] = 0
stk = [n]
while dp[k] == float('inf'):
    tmp = []
    for i in stk:
        while i*2 <= 100000:
            if dp[i] < dp[i*2]:
                dp[i*2] = dp[i]
                i *= 2
                tmp.append(i)
            else:
                break
    stk += tmp
    tmp = []
    while stk:
        now = stk.pop()
        for i in (now-1, now+1):
            if 0<=i<=100000 and dp[i] == float('inf'):
                dp[i] = dp[now]+1
                tmp.append(i)
    stk = tmp
print(dp[k])