from math import ceil


gets = [int(input()) for _ in range(5)]
a = ceil(gets[1]/gets[3])
b = ceil(gets[2]/gets[4])

if a > b:
    print(gets[0] - a)
else:
    print(gets[0] - b)