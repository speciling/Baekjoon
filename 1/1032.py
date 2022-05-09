from sys import stdin

n = int(stdin.readline())
files = [stdin.readline().strip() for _ in range(n)]
ans = []

for i in range(len(files[0])):
    c = files[0][i]
    ans.append(c)
    for j in range(1, n):
        if c == files[j][i]:
            continue
        else:
            ans[i] = '?'

print(''.join(ans))
