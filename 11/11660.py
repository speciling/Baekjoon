from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        nums[i][j] += nums[i][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        nums[i][j] += nums[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = nums[x2][y2] - nums[x2][y1-1] - nums[x1-1][y2] + nums[x1-1][y1-1]
    print(total)