n = int(input())
f = [0, 1]
if n == 0:
    print(n)
elif n == 1:
    print(1)
else:
    for i in range(0, n-1):
        f.append((f[i]+f[i+1]))
    print(f[-1])