from sys import stdin

n, m = map(int, stdin.readline().split())
passwords = {}
for _ in range(n):
    site, password = stdin.readline().rstrip().split()
    passwords[site] = password
for _ in range(m):
    print(passwords[stdin.readline().rstrip()])
