from sys import stdin

for _ in range(int(input())):
    arr = sorted(list(map(int, stdin.readline().split())))
    print(arr[-3])