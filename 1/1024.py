n, l = map(int, input().split())
ans = [-1]
for i in range(l, 101):
    first = i*(i-1) // 2
    if (n - first) % i == 0:
        start = (n - first) // i
        if start >= 0:
            ans = list(range(start, start+i))
            break
print(*ans)
