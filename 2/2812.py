import sys
n, k = map(int, sys.stdin.readline().split())
ans = ['9']
for i in sys.stdin.readline().rstrip():
    while k > 0 and i > ans[-1]:
        ans.pop()
        k -= 1
    ans.append(i)
print(''.join(ans[1:-k] if k else ans[1:]))