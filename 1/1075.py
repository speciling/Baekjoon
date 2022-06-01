n = int(input())
f = int(input())

x = int(str(n)[:-2]) * 100
n += (f - (n % f))

while True:
    if n - f >= x:
        n -= f
    else:
        print(str(n)[-2:])
        break