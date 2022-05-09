from sys import stdin
n, m, b = map(int, stdin.readline().split())
ground = []

for _ in range(n):
    ground.extend(list(map(int, stdin.readline().split())))

max_h = int((sum(ground) + b) / (n*m))
if max_h > 256:
    max_h = 256
min_h = min(ground)

ans = []
for i in range(min_h, max_h + 1):
    time = 0
    for j in range(n*m):
        if ground[j] > i:
            time += 2*(ground[j] - i)
        elif ground[j] < i:
            time += i - ground[j]
    ans.append((time, i))

ans.sort(key=lambda x: (x[0], -x[1]))

print(ans[0][0], ans[0][1])