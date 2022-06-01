get = input()
boom = list(input())
stack = []
x = len(boom)

for s in get:
    stack.append(s)
    if s == boom[-1]:
        if stack[-x:] == boom:
            for _ in range(x):
                stack.pop()

print(''.join(stack) if stack else 'FRULA')