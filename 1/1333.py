N, L, D = map(int, input().split())

time = 0
ans = 0
while N:
    N -= 1
    time += L
    for i in range(time, time + 5):
        if i % D == 0:
            ans = i
            break
    else:
        time += 5
    if ans:
        break
if ans != 0:
    print(ans)
else:
    while True:
        if time % D == 0:
            print(time)
            break
        time += 1
