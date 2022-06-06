from sys import stdin
target = {'a', 'e', 'i', 'o', 'u'}
while True:
    s = stdin.readline().lower().rstrip()
    cnt = 0
    if s == '#':
        break
    else:
        for i in s:
            if i in target:
                cnt += 1
        print(cnt)