from collections import deque


def find_turn(m, importance):
    que = deque(importance)
    turn = 0
    maximum = max(que)
    while que:
        if que[0] == maximum:
            que.popleft()
            turn += 1
            if m == 0:
                print(turn)
                break
            maximum = max(que)
        else:
            que.append(que.popleft())
        m = m-1 if m else len(que)-1


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    find_turn(m, importance)
