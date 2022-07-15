from sys import stdin

for tc in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    ans = 1
    for i in range(m, m-n, -1):
        ans *= i
    for j in range(1, n+1):
        ans //= j
    print(ans)