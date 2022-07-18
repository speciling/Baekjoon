n = int(input())
nums = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.insert(i-nums[i], i+1)
print(*arr)