tree = map(int, open(0).read().split())
stk = [[next(tree), float('inf')]]
for node in tree:
    if node > stk[-1][0]:
        while node > stk[-1][1]:
            print(stk.pop()[0])
        stk.append([node, stk[-1][-1]])
    else:
        stk.append([node, stk[-1][0]])
[print(i[0]) for i in reversed(stk)]