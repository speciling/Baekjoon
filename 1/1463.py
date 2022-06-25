def make1(n):
    if n in ans:
        return ans[n]
    ans[n] = min(make1(n//3) + n % 3, make1(n//2) + n % 2) + 1
    return ans[n]


ans = {1: 0, 2: 1}
print(make1(int(input())))
