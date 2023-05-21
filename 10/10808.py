S = input()
cnt = [0] * 26
for s in S:
    cnt[ord(s)-97] += 1
print(*cnt)
