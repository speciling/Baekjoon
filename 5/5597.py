nums = set(range(1,31))
for _ in range(28):
    nums.remove(int(input()))
print(f'{min(nums)}\n{max(nums)}')