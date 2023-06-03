k = int(input())
move = []
flag = False
for i in range(6):
    a, b = map(int, input().split())
    move.append(b)
big = 1
small = 1
for i in (move[::2], move[1::2]):
    big *= max(i)
    small *= move[(move.index(max(i))+3)%6]
print((big-small)*k)