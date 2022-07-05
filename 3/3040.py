nums = [int(input()) for _ in range(9)]
target = sum(nums) - 100
for i in range(8):
    if len(nums) != 9:
        break
    for j in range(1, 9 - i):
        if nums[i] + nums[i+j] == target:
            nums.pop(i)
            nums.pop(i+j-1)
            break
for num in nums:
    print(num)
