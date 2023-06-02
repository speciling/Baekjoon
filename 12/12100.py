def left(board):
    res = []
    for line in board:
        tmp = []
        p = 0
        prev = -1
        while p < len(line):
            if line[p] != 0:
                if line[p] != prev:
                    tmp.append(line[p])
                    prev = line[p]
                else:
                    tmp.append(tmp.pop()*2)
                    prev = -1
            p += 1
        tmp += [0]*(len(line)-len(tmp))
        res.append(tmp)
    return res


def right(board):
    res = left([list(reversed(i)) for i in board])
    return [list(reversed(i)) for i in res]


def up(board):
    res = left([list(i) for i in zip(*board)])
    return [list(i) for i in zip(*res)]


def down(board):
    res = right([list(i) for i in zip(*board)])
    return [list(i) for i in zip(*res)]


def solve(board, n):
    if n == 0:
        return max(max(i) for i in board)

    return max(solve(left(board), n-1), solve(right(board), n-1), solve(up(board), n-1), solve(down(board), n-1))


print(solve([list(map(int, input().split())) for _ in range(int(input()))], 5))