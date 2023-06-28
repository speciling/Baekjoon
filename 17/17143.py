from sys import stdin
input = stdin.readline


def init():
    r, c, m = map(int, input().split())
    board = [[0] * c for _ in range(r)]
    sharks = {}
    for i in range(1, m + 1):
        s = list(map(int, input().split()))
        s[0] -= 1
        s[1] -= 1
        s[2] = s[2]%((r-1)*2) if s[3]<3 else s[2]%((c-1)*2)
        board[s[0]][s[1]] = i
        sharks[i] = s
    return r, c, sharks, board


def fishing(sharks, board, n):
    for i in range(len(board)):
        if board[i][n] > 0:
            size = sharks[board[i][n]][4]
            del sharks[board[i][n]]
            board[i][n] = 0
            return size
    return 0


def moveshark(sharks, r, c):
    board = [[0] * c for _ in range(r)]
    for i in list(sharks.keys()):
        x, y, s, d, z = sharks[i]
        if d < 3:
            x += s if d == 2 else -s
            if x < 0:
                x *= -1
                d = 2
                if x > r-1:
                    x = 2*(r-1) - x
                    d = 1
            elif x > r-1:
                x = 2 * (r - 1) - x
                d = 1
                if x < 0:
                    x *= -1
                    d = 2
        else:
            y += s if d == 3 else -s
            if y < 0:
                y *= -1
                d = 3
                if y > c-1:
                    y = 2*(c-1) - y
                    d = 4
            elif y > c-1:
                y = 2*(c-1) - y
                d = 4
                if y < 0:
                    y *= -1
                    d = 3
        if board[x][y]:
            if sharks[board[x][y]][4] > z:
                del sharks[i]
                continue
            else:
                del sharks[board[x][y]]
        board[x][y] = i
        sharks[i] = [x, y, s, d, z]
    return board


def solve():
    r, c, sharks, board = init()
    cnt = 0
    for i in range(c):
        cnt += fishing(sharks, board, i)
        board = moveshark(sharks, r, c)
    return cnt


print(solve())

