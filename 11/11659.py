from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
i_to_j = [list(map(int, stdin.readline().split())) for _ in range(m)]

nums_sum = [0]
for i in range(n):
    nums_sum.append(nums_sum[i] + nums[i])

for i in range(m):
    print(nums_sum[i_to_j[i][1]] - nums_sum[i_to_j[i][0]-1])