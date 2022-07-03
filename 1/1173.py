N, m, M, T, R = map(int, input().split())

if T > M-m:
    print(-1)
else:
    time = 0
    pulse = m
    while N != 0:
        time += 1
        if pulse + T <= M:
            N -= 1
            pulse += T
        else:
            pulse -= R
            if pulse < m:
                pulse = m
    print(time)
