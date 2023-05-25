n, m = map(int, input().split())
def dfs(s, e, num, stk):
    if num == 0:
        print(*stk)
        return
    for i in range(s, e+1):
        stk.append(i)
        dfs(i, e, num-1, stk)
        stk.pop()
dfs(1, n, m, [])