s = input()
arr = []
for i in range(len(s)):
    arr.append(s[i:])
arr.sort()
print('\n'.join(arr))