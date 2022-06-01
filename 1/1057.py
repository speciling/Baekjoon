n, a, b = map(int, input().split())
a -= 1
b -= 1
for i in range(1, 18):
    if a//(2**i) == b//(2**i):
        print(i)
        break