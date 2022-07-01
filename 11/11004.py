from sys import stdin

n, k = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
print(nums[k-1])