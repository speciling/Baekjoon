from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print('\n'.join(map(' '.join, combinations_with_replacement(map(str, nums), m))))