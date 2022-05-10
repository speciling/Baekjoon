n = int(input())
arr = list(map(int, input().split()))
stack = []
nge = [-1] * n

for i, num in enumerate(arr):
    while stack:
        if stack[-1][0] < num:
            nge[stack[-1][1]] = num
            stack.pop()
        else:
            break
    stack.append([num, i])

print(*nge)