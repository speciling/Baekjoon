from sys import stdin

n = int(stdin.readline())
nums = [0] * 10001
for _ in range(n):
    nums[int(stdin.readline())] += 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)