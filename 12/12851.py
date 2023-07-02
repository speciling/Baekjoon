from collections import deque
n, k = map(int, input().split())
q = deque([n])
visited = [-1]*100001
visited[n] = 0
time = 0
ways = 0

while q:
    now = q.popleft()
    if now == k:
        time = visited[now]
        ways = q.count(k)+1
        break
    for i in (now-1, now+1, now*2):
        if 0 <= i <= 100000 and (visited[i] == -1 or visited[i] == visited[now]+1):
            q.append(i)
            visited[i] = visited[now]+1

print(time)
print(ways)