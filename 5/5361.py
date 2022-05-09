from sys import stdin

price = [35034, 23090, 19055, 12530, 18090]
n = int(stdin.readline())
case = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
    ans = 0
    for j in range(5):
        ans += (case[i][j] * price[j]) / 100
    print(f'${ans:.2f}')