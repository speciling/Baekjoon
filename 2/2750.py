from sys import stdin

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]
nums.sort()

for num in nums:
    print(num)