from sys import stdin

for _ in range(int(input())):
    sx, sy, ax, ay = map(int, stdin.readline().split())
    count = 0
    for _ in range(int(stdin.readline())):
        cx, cy, r = map(int, stdin.readline().split())
        if ((cx-sx)**2 + (cy-sy)**2 < r**2) != ((cx-ax)**2 + (cy-ay)**2 < r**2):
            count += 1
    print(count)