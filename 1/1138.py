n = int(input())
arr = list(map(int, input().split()))
ans = [n]
for i in range(2, n+1):
    ans.insert(arr[-i], n+1-i)
print(*ans)
