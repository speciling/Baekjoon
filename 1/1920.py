from sys import stdin
input = stdin.readline

input()
ns = set(input().split())
input()

for m in input().split():
    if m in ns:
        print(1)
    else:
        print(0)
