from sys import stdin

n, m = map(int, stdin.readline().split())
price = [1001, 1001]
for _ in range(m):
    temp = list(map(int, stdin.readline().split()))
    for i in range(2):
        if temp[i] < price[i]:
            price[i] = temp[i]
print(min(price[0]*(n//6)+price[1]*(n%6), price[1]*n, price[0]*(n//6+1)))