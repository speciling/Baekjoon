n = int(input())
for i in range(n-1):
    print(' '*i + '*'*(2*n-1-2*i))
for i in range(n-1, -1, -1):
    print(' '*i + '*'*(2*n-1-2*i))