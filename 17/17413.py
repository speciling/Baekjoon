s = input().replace('>', '<').split('<')
ans = ''
for i in range(len(s)):
    if i % 2:
        ans += '<'+s[i]+'>'
    else:
        words = s[i].split()
        ans += ' '.join([word[::-1] for word in words])
print(ans)