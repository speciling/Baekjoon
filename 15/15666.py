from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = sorted(map(int, set(input().split())))
for i in combinations_with_replacement(nums, m):
    print(*i)