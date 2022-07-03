from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 1
end = 10 ** 9

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
