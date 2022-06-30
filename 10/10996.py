n = int(input())
for i in range(n):
    if n == 1:
        print('*')
    else:
        m = n//2 if n % 2 == 0 else n//2 + 1
        print('*' + ' *' * (m-1))
        print(' *' * (n//2))