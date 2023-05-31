from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    dp = [0, 0, 0]
    for s1, s2 in zip(map(int, input().split()), map(int, input().split())):
        dp = [max(dp), max(dp[0], dp[2])+s1, max(dp[0], dp[1])+s2]
    print(max(dp))