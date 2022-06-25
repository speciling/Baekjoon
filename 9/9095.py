def a(n):
    if n in cache:
        return cache[n]
    return a(n-1) + a(n-2) + a(n-3)


cache = {1: 1, 2: 2, 3: 4}
for _ in range(int(input())):
    print(a(int(input())))
