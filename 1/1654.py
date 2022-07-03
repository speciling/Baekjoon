from sys import stdin

n, k = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]
start = 1
end = max(arr)
max_len = -1

while start <= end:
    mid = (start + end) // 2
    m = 0
    for i in arr:
        m += i//mid
    if m >= k:
        max_len = mid
        start = mid + 1
    else:
        end = mid - 1
print(max_len)
