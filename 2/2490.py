res = ['E', 'A', 'B', 'C', 'D']
for i in range(3):
    s = sum(map(int, input().split()))
    print(res[4-s])