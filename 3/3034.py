n, w, h = map(int, input().split())
l = [int(input()) for _ in range(n)]
m = w**2 + h**2
for i in l:
    if i**2 <= m:
        print("DA")
    else:
        print("NE")