n = int(input())
children = [[] for _ in range(n+1)]
for i, n in enumerate(map(int, input().split())):
    children[n].append(i)
d = int(input())

root = children[-1][0]
cnt = 0
if root != d:
    stk = [root]
    while stk:
        now = stk.pop()
        if children[now] and (children[now][0] != d or len(children[now]) >= 2):
            for i in children[now]:
                if i != d:
                    stk.append(i)
        else:
            cnt += 1
print(cnt)