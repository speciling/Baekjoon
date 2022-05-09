h, m, s = map(int, input().split())
t = int(input())

s += t % 60
m += (t // 60) + s // 60
h += m // 60

s %= 60
m %= 60
h %= 24

print(h, m, s)
