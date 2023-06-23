from collections import Counter
c = Counter(input())
nums = [c[i] for i in "0123456789"]
if not nums[0] or sum(nums[i]*i for i in range(10))%3:
    print(-1)
else:
    print(''.join(str(i)*nums[i] for i in range(9,-1,-1)))