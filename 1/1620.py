from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(n)]
d = {arr[i]: i+1 for i in range(n)}

for _ in range(m):
    x = stdin.readline().rstrip()
    if x.isdigit():
        print(arr[int(x)-1])
    else:
        print(d[x])