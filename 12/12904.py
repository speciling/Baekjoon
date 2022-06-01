a = input()
b = list(input())

for _ in range(len(b)-len(a)):
    if b[-1] == 'A':
        b.pop()
    else:
        b.pop()
        b.reverse()

if a == ''.join(b):
    print(1)
else:
    print(0)