from itertools import product
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print('\n'.join(map(' '.join, product(map(str, nums), repeat=m))))