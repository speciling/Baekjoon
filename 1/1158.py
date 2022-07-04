n, k = map(int, input().split())
peoples = list(range(1, n+1))
x = 0
k -= 1
ans = []
while peoples:
    x = (x + k) % n
    ans.append(peoples.pop(x))
    n -= 1
    if x == n:
        x = 0

print('<' + str(ans)[1:-1] + '>')

