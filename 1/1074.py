def z(x, y, n):
    if n == 1:
        return x * 2 + y
    else:
        temp = (0, 2**(n-1), 2**n)
        if 0 <= x < 2**(n-1):
            if 0 <= y < 2**(n-1):
                return z(x, y, n-1)
            else:
                y -= 2**(n-1)
                return 2**(n-1) * 2**(n-1) + z(x, y, n-1)
        else:
            if 0 <= y < 2 ** (n - 1):
                x -= 2**(n-1)
                return 2**(n-1) * 2**(n-1) * 2 + z(x, y, n - 1)
            else:
                x -= 2 ** (n - 1)
                y -= 2 ** (n - 1)
                return 2**(n-1) * 2**(n-1) * 3 + z(x, y, n - 1)


N, c, r = map(int, input().split())
print(z(c, r, N))
