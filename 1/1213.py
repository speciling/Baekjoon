alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
gets = [0]*26
p = ''
odds = 0
mid = ''
for i in input():
    gets[alp.index(i)] += 1
for i in range(26):
    if gets[i] % 2:
        odds += 1
        if odds > 1:
            break
        mid = alp[i]
    p += alp[i] * (gets[i]//2)
if odds > 1:
    print("I'm Sorry Hansoo")
else:
    print(p+mid+p[::-1])