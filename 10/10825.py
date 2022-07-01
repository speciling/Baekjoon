from sys import stdin

n = int(stdin.readline())
s = []
for _ in range(n):
    get = stdin.readline().strip().split()
    s.append([get[0]] + list(map(int, get[1:])))
s.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in s:
    print(i[0])