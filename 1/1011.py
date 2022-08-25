from sys import stdin

for tc in range(int(input())):
    x, y = map(int, stdin.readline().split())
    to_move = y - x
    moved = 0
    cnt = 0
    i = 1
    while to_move > moved:
        cnt += 1
        moved += i
        if to_move <= moved:
            break

        cnt += 1
        moved += i
        i += 1
    print(cnt)