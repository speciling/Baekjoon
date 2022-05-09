N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

for i in range(N-2):
    a = nums[i]
    for j in range(i+1, N):
        b = nums[j]
        for k in range(j+1, N):
            c = nums[k]
            if a+b+c <= M:
                ans.append(a+b+c)
            else:
                break

print(max(ans))