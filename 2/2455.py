gets = [list(map(int, input().split())) for _ in range(4)]
passenger = [gets[i][1] - gets[i][0] for i in range(4)]

for i in range(1,4):
    passenger[i] += passenger[i - 1]

print(max(passenger))