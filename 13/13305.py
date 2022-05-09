from sys import stdin

n = int(stdin.readline())
distance = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
price_index = sorted([[price[i], i] for i in range(n)])

min_price = price_index[0][0]
city_num = price_index[0][1]
cost = sum(distance[city_num:]) * min_price

for i in range(1,n):
    if price_index[i][1] < city_num:
        min_price = price_index[i][0]
        n_city_num  = price_index[i][1]
        cost += sum(distance[n_city_num:city_num]) * min_price
        city_num = n_city_num

print(cost)