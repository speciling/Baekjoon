import sys
input = sys.stdin.readline

n, c = map(int, input().split())
dic = {i: [] for i in range(1, n)}
for _ in range(int(input())):
    send, receive, num = map(int, input().split())
    dic[send].append((receive, num))
capacity = [c]*(n+1)

cnt, end = 0, n
for send in range(n-1,0,-1):
    if not dic[send]:
        continue
    dic[send].sort(reverse=True)
    for receive, num in dic[send]:
        if receive <= end and capacity[receive]:
            for i in range(receive, send, -1):
                if capacity[i] <= num:
                    end, num = i, capacity[i]
            receive = min(receive, end)
            capacity[send+1:receive+1] = map(lambda x: x-num, capacity[send+1:receive+1])
            cnt += num

print(cnt)