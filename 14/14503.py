dir = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 방향(북,동,남,서)
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]  # 0:청소x, 1:벽, 2:청소o
cnt = 0

while True:
    # 1번과정
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    # 2번과정
    # 2-a
    for _ in range(4):
        d = d - 1 if d > 0 else 3
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < n and 0 <= nc < m:
            if room[nr][nc] == 0:
                r, c = nr, nc
                break
    # 2-b
    else:
        nr = r - dir[d][0]
        nc = c - dir[d][1]
        if 0 <= nr < n and 0 <= nc < m:
            if room[nr][nc] == 1:
                break
            else:
                r, c = nr, nc

print(cnt)