from sys import stdin
n = int(input())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
white, blue = 0, 0


def divide(graph):
    global white, blue
    length = len(graph)
    s = graph[0][0]
    for i in graph:  # 같은 색으로 칠해졌는지 확인. 다른색 있으면 break
        for j in i:
            if j != s:
                s = -1
                break
        if s == -1:
            break
    else:  # 같은색만 있으면 return 흰, 파
        if s == 0:
            white += 1
            return
        else:
            blue += 1
            return
    # 다른 색 있으면 분할
    a, b, c, d = [], [], [], []
    for i in range(length//2):
        a.append(graph[i][:length//2])
        b.append(graph[i][length//2:])
    for i in range(length//2, length):
        c.append(graph[i][:length // 2])
        d.append(graph[i][length // 2:])
    divide(a)
    divide(b)
    divide(c)
    divide(d)


divide(paper)
print(f'{white}\n{blue}')
