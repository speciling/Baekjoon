n, m = map(int, input().split())
a, b = 1, 1
for i in range(m):
    a *= (n-i)
    b *= (i+1)
print(int(a/b))