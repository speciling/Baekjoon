n = int(input())
d = [5] * (n+1)
i = 1
sn = []  # square num -> 제곱수
for i in range(1, int(n**0.5) + 1):
    d[i**2] = 1
    sn.append(i**2)
for i in range(2, n+1):
    if d[i] == 1:
        continue
    for j in sn:
        if j < i:
            d[i] = min(d[i], d[i-j] + 1)
            if d[i] == 2:
                break
print(d[n])