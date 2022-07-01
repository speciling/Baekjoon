from sys import stdin

n = int(stdin.readline())
nums = [0] * 10001
for _ in range(n):
    nums[int(stdin.readline())] += 1
max_weight = 0
cnt = 0
for i in range(1, 10001):
    if nums[i]:
        max_weight = max(max_weight, i*(n-cnt))
        cnt += nums[i]
print(max_weight)
