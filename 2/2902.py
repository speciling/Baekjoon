names = list(input().split('-'))
ans = ''

for i in range(len(names)):
    ans += names[i][0]

print(ans)