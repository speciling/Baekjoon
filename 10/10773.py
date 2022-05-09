from sys import stdin

k = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(k)]
stack = []

for i in range(k):
    if nums[i]:
        stack.append(nums[i])
    else:
        stack.pop()

print(sum(stack))