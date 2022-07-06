m = int(input()); n = int(input())
nums = []
for i in range(1, 101):
    if m <= i**2 <= n:
        nums.append(i**2)
if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)
