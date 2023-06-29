import sys

arr = []
max_dp, min_dp = [0]*3, [0]*3

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, input().rstrip().split())
    max_dp = (max(max_dp[:2]) + a, max(max_dp) + b, max(max_dp[1:]) + c)
    min_dp = (min(min_dp[:2]) + a, min(min_dp) + b, min(min_dp[1:]) + c)

print(max(max_dp), min(min_dp))