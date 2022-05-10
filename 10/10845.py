from collections import deque
from sys import stdin

n = int(stdin.readline())
que = deque()
gets = [stdin.readline().strip().split() for _ in range(n)]
for get in gets:
    if get[0] == 'push':
        que.append(get[1])
    elif get[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif get[0] == 'size':
        print(len(que))
    elif get[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif get[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif get[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)