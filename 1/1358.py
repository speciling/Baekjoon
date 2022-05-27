from sys import stdin

w, h, x, y, p = map(int, stdin.readline().split())
r = h/2
count = 0
for _ in range(p):
    px, py = map(int, stdin.readline().split())
    if x <= px <= x+w and y <= py <= y+h:
        count += 1
    elif (x-px)**2 + (y+r-py)**2 <= r**2 or (x+w-px)**2 + (y+r-py)**2 <= r**2:
        count += 1
print(count)
