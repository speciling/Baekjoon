from sys import stdin

n = int(stdin.readline())
names = [stdin.readline().rstrip() for _ in range(n)]
names.sort()
count = 0
ans = ''
for i in range(1,n):
    if names[i][0] == names[i-1][0]:
        count += 1 if count != 0 else 2
    else:
        count = 0
    if count == 5:
        ans += names[i][0]

print(ans if ans else 'PREDAJA')