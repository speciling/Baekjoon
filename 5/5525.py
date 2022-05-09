n = int(input())
m = int(input())
s = input()

ans = 0
i = 0
IOI = 0
while i < m-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        IOI += 1
        if IOI == n:
            ans += 1
            IOI -= 1
        i += 2
    else:
        IOI = 0
        i += 1

print(ans)
