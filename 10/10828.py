from sys import stdin

stack = []
n = int(stdin.readline())
gets = [stdin.readline().strip().split() for _ in range(n)]

for i in range(n):
    if gets[i][0] == 'push':
        stack.append(gets[i][1])
    elif gets[i][0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif gets[i][0] == 'size':
        print(len(stack))
    elif gets[i][0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])