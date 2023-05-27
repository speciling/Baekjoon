from itertools import permutations
from sys import stdout
print = stdout.write
n, m = map(int, input().split())
for i in sorted(set(permutations(map(int, input().split()), m))):
    print(' '.join(map(str, i)) + '\n')