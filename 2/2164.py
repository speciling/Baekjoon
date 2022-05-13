from collections import deque

n = int(input())
que = deque(i for i in range(1, n+1))

for _ in range(n-1):
    que.popleft()
    que.append(que.popleft())

print(que.pop())