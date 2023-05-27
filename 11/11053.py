import bisect

input()
dp = [0]

for i in map(int, input().split()):
    if i > dp[-1]:
        dp.append(i)
    else:
        dp[bisect.bisect_left(dp, i)] = i

print(len(dp)-1)