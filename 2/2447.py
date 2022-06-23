def stars(n):
    global ans
    if n == 3:
        ans[0][:3] = ans[2][:3] = ['*']*3
        ans[1][:3] = ['*', ' ', '*']
        return
    x = n//3
    stars(x)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(x):
                ans[x*i+k][x*j:x*(j+1)] = ans[k][:x]


n = int(input())
ans = [[' ' for _ in range(n)] for _ in range(n)]
stars(n)
for i in ans:
    print(''.join(i))