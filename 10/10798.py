words = [input() for _ in range(5)]
ans = {}
for i in range(5):
    j = 1
    for s in words[i]:
        if j in ans:
            ans[j] += s
        else:
            ans[j] = s
        j += 1
for i in ans.values():
    print(i, end='')