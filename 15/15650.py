from itertools import combinations
n, m = map(int, input().split())
print('\n'.join(' '.join(map(str, i)) for i in combinations(range(1, n+1), m)))