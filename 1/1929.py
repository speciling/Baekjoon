m, n = map(int, input().split())
nums = [True for _ in range(n+1)]
nums[1] = False

for i in range(2, int(n**0.5) + 1):
    if nums[i]:
        j = 2
        while j * i <= n:
            nums[j*i] = False
            j += 1

for i in range(m,n+1):
    if nums[i]:
        print(i)