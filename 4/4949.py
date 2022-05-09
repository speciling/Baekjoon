from sys import stdin

gets = []
while True:
    gets.append(stdin.readline().rstrip())
    if gets[-1] == '.':
        gets.pop()
        break

for i in range(len(gets)):
    stack = []
    for j in gets[i]:
        if j == '[' or j == '(':
            stack.append(j)
        elif j == ']' or j == ')':
            if stack:
                if j == ')' and stack[-1] == '(':
                    stack.pop()
                elif j == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')