from itertools import combinations
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
print('\n'.join(' '.join(map(str, i)) for i in combinations(nums, m)))