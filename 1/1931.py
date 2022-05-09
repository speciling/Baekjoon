from sys import stdin

n = int(stdin.readline())
gets = [list(map(int, stdin.readline().split())) for _ in range(n)]
gets = sorted(gets, key=lambda gets: (gets[1], gets[0]))

start_time = [gets[i][0] for i in range(n)]
end_time = [gets[i][1] for i in range(n)]

time = end_time[0]
count = 1

for i in range(1, n):
    if start_time[i] >= time:
        time = end_time[i]
        count += 1

print(count)
