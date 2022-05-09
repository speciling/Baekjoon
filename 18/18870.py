n = int(input())
nums = list(map(int, input().split()))
comp = sorted(list(set(nums)))
ans = []
for i in nums:
    ans.append(str(comp.index(i)))

print(' '.join(ans))