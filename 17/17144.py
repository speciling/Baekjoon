from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if A[i][0] == -1:
        ac = i
        break

def diffused(room):
    nroom = [i[:] for i in room]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(r):
        for j in range(c):
            if room[i][j]>0:
                diffussion = room[i][j]//5
                for m in move:
                    nr, nc = i+m[0], j+m[1]
                    if 0<=nr<r and 0<=nc<c and room[nr][nc] != -1:
                        nroom[i][j] -= diffussion
                        nroom[nr][nc] += diffussion

    return nroom

def blow(room, ac):
    move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    prev = 0
    nr, nc = ac, 0
    for m in move:
        while True:
            if 0<=nr+m[0]<r and 0<=nc+m[1]<c and room[nr+m[0]][nc+m[1]] != -1:
                nr, nc = nr+m[0], nc+m[1]
                room[nr][nc], prev = prev, room[nr][nc]
            else:
                break

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    prev = 0
    nr, nc = ac+1, 0
    for m in move:
        while True:
            if 0<=nr+m[0]<r and 0<=nc+m[1]<c and room[nr+m[0]][nc+m[1]] != -1:
                nr, nc = nr+m[0], nc+m[1]
                room[nr][nc], prev = prev, room[nr][nc]
            else:
                break

for _ in range(t):
    A = diffused(A)
    blow(A, ac)

print(sum(sum(i) for i in A)+2)