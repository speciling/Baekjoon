from sys import stdin

n = int(stdin.readline())
members = [stdin.readline().strip().split() for _ in range(n)]
members.sort(key=lambda x: int(x[0]))
print('\n'.join(list(map(' '.join, members))))