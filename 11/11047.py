from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
count = 0
i = 1

while k != 0:
    count += k // coins[-i]
    k %= coins[-i]
    i += 1

print(count)