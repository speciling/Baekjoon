n = int(input())
a = list(enumerate(list(map(int, input().split()))))
a.sort(key=lambda x: x[1])
b = sorted(list(enumerate(a)), key=lambda x: x[1][0])

p = [x[0] for x in b]
print(' '.join(map(str, p)))


'''
n = int(input())
l = list(map(int, input().split()))
s = [0]*n

for i in range(n):
    k = l.index(min(l))
    s[k] = i
    l[k] = 1001
    
print(*s)
'''