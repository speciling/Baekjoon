from sys import stdin

n, m = map(int, stdin.readline().split())
a = {stdin.readline().rstrip() for _ in range(n)}
b = {stdin.readline().rstrip() for _ in range(m)}
ans = list(a&b)
print(len(ans))
print('\n'.join(sorted(ans)))
