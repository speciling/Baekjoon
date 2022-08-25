a, b = input().split()
n = int(a.replace('6', '5')) + int(b.replace('6', '5'))
m = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(n, m)