a, b, c = map(int, input().split())
n = 1
while b:
    if b % 2:
        n = (n*a)%c
        b -= 1
    else:
        a = (a*a)%c
        b //= 2
print(n)