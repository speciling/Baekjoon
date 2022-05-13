n, k = map(int, input().split())
people = list(range(1, n+1))
ans = []
i = 0
k -= 1
for _ in range(n):
    if i == n:
        i = 0
    i = (i + k) % n
    ans.append(people.pop(i))
    n -= 1

print(str(ans).replace('[', '<').replace(']', '>'))