from sys import stdin

N = int(stdin.readline())

people = []
for _ in range(N):
    people.append(list(map(int, stdin.readline().split())))

ans = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            ans[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ans[i] += 1

for i in range(N):
    print(ans[i], end=' ')