def make1(n):
    if n in d:
        return d[n]
    d[n] = min(make1(n//3) + n % 3, make1(n//2) + n % 2) + 1
    return d[n]


d = {1: 0, 2: 1}
n = int(input())
print(make1(n))
ans = [n]
while n != 1:
    if d[n] == d[n//2] + n % 2 + 1:
        if n % 2:
            n -= 1
            ans.append(n)
        n //= 2
        ans.append(n)
    elif d[n] == d[n//3] + n % 3 + 1:
        while n % 3:
            n -= 1
            ans.append(n)
        n //= 3
        ans.append(n)
print(*ans)