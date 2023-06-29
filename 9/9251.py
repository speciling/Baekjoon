s1, s2 = input(), input()
dp = [0]*(len(s2)+1)
for i in range(len(s1)):
    tmp = [0]*(len(s2)+1)
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            tmp[j+1] = dp[j]+1
        else:
            tmp[j+1] = max(tmp[j], dp[j+1])
    dp = tmp
print(dp[-1])