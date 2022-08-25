from sys import stdin


def dp(num):
    if d[num]:
        return d[num]
    else:
        d[num] = dp(num-1) + dp(num-5)
        return d[num]


d = [0] * 101
d[:5] = [1, 1, 1, 2, 2]
for tc in range(int(input())):
    n = int(stdin.readline())
    print(dp(n-1))
