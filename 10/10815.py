from sys import stdin
input = stdin.readline

input()
n = set(input().split())
input()
ans = ''
for i in input().split():
    ans += '1 ' if i in n else '0 '
print(ans)
