from sys import stdin

n, m = map(int, stdin.readline().split())
nums = [list(stdin.readline().strip()) for _ in range(n)]
size = 1

for i in range(n-1):
    for j in range(m-1):
        for k in range(j+1, m):
            if nums[i][j] == nums[i][k]:
                if k-j <= n-1-i:
                    if nums[i][j] == nums[i+k-j][j] and nums[i][j] == nums[i+k-j][k]:
                        if (k-j+1)**2 > size:
                            size = (k-j+1)**2

print(size)