from sys import stdin

N, L = map(int, stdin.readline().split())
leak = sorted((list(map(int, stdin.readline().split()))))
tape = 0
cnt = 0
for i in leak:
    if i > tape:
        tape = i + L - 1
        cnt += 1
print(cnt)