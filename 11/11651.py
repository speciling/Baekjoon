from sys import stdin

n = int(stdin.readline())
coordinates = [list(map(int, stdin.readline().split())) for _ in range(n)]
coordinates.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(coordinates[i][0], coordinates[i][1])