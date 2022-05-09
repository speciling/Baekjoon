get = input()
i = 0
nums = []
while True:
    i = get.find('-')
    if i == -1:
        nums.append(sum(map(int, get.split('+'))))
        break
    else:
        nums.append(sum(map(int, get[:i].split('+'))))
        get = get[i+1:]

ans = nums[0]
for j in range(1,len(nums)):
    ans -= nums[j]

print(ans)