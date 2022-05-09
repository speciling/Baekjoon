def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


i = 1
s = str(factorial(int(input())))
while s[-i] == '0':
    i += 1

print(i-1)