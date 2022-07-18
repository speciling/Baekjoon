from sys import stdin

for tc in range(int(stdin.readline())):
    n = int(stdin.readline())
    clothes = {}
    for _ in range(n):
        a, b = stdin.readline().split()
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 1
    ans = 1
    for i in clothes.values():
        ans *= i + 1
    print(ans-1)