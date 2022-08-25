from sys import stdin

for tc in range(int(stdin.readline())):
    n = int(stdin.readline())
    prison = [-1] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            prison[j] *= -1
    print(prison.count(1))
