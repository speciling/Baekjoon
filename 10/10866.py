from collections import deque
from sys import stdin

n = int(stdin.readline())
orders = [stdin.readline().split() for _ in range(n)]
deq = deque()

for order in orders:
    if order[0] == 'push_front':
        deq.appendleft(order[1])
    elif order[0] == 'push_back':
        deq.append(order[1])
    elif order[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif order[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        print(0 if deq else 1)
    elif order[0] == 'front':
        print(deq[0] if deq else -1)
    elif order[0] == 'back':
        print(deq[-1] if deq else -1)
