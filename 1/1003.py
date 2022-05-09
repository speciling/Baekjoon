from sys import stdin

t = int(stdin.readline())

for i in range(t):
    case = [0] * 41
    case[int(stdin.readline())] = 1
    for j in range(40,1,-1):
        case[j-1] += case[j]
        case[j-2] += case[j]
    print(case[0], case[1])