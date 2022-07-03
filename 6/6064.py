from sys import stdin
from math import lcm


def crt(arr):
    a, b, x, y = arr
    if a == x and b == y:
        return lcm(a, b)
    if a == x:
        x = 0
    if y == b:
        y = 0
    if a > b:
        a, b = b, a
        x, y = y, x
    for i in range(b):
        if (a * i + x) % b == y:
            return a * i + x
    return -1


for i in range(int(stdin.readline())):
    gets = map(int, stdin.readline().split())
    print(crt(gets))