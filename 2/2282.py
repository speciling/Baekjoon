scores = [[int(input()), i] for i in range(1, 9)]
scores.sort()
ans = []
s = 0
for i in scores[3:]:
    s += i[0]
    ans.append(i[1])
print(s)
print(*sorted(ans))