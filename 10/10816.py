from sys import stdin

stdin.readline()
dic = {}
for i in map(int, stdin.readline().split()):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
stdin.readline()
for num in map(int, stdin.readline().split()):
    print(dic[num] if num in dic else 0, end=' ')