from sys import stdin

t = int(stdin.readline())
gets = [stdin.readline().strip() for _ in range(t)]
for i in range(t):
    stack = [0]
    for j in range(len(gets[i])):
        if gets[i][j] == '(':
            stack.append('(')
        else:
            if stack[-1] == 0:
                stack.append(1)
                break
            else:
                stack.pop()
    if stack[-1] == 0:
        print('YES')
    else:
        print('NO')