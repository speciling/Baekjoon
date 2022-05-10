from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

stack = []
ans = []
x = 0
for i in range(1, n+1):
    while stack:
        if stack[-1] == arr[x]:
            stack.pop()
            x += 1
            ans.append('-')
        else:
            break
    if arr[x] == i:
        x += 1
        ans += ['+', '-']
    else:
        stack.append(i)
        ans.append('+')

while stack:
    if stack[-1] == arr[x]:
        stack.pop()
        x += 1
        ans.append('-')
    else:
        break

if stack:
    print('NO')
else:
    print('\n'.join(ans))