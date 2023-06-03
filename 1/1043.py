from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
_, *know = map(int, input().split())

if not know:
    [input() for _ in range(m)]
    print(m)
else:
    graph = [[] for _ in range(n + 1)]
    parties = []
    for _ in range(m):
        num, *party = map(int, input().split())
        parties.append(party)
        for i in range(num):
            for j in range(i+1, num):
                graph[party[i]].append(party[j])
                graph[party[j]].append(party[i])
    visited = [False]*(n+1)
    stk = know
    know = set()
    for i in stk:
        if not visited[i]:
            visited[i] = True
            stk += graph[i]
            know.add(i)

    cnt = 0
    for party in parties:
        for p in party:
            if p in know:
                break
        else:
            cnt += 1
    print(cnt)