from sys import stdin

while True:
    s = stdin.readline().lower().rstrip()
    ans = 0
    if s == '#':
        break
    else:
        ans += s.count('a')
        ans += s.count('e')
        ans += s.count('i')
        ans += s.count('o')
        ans += s.count('u')
        print(ans)