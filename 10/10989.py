import sys
c = [0]*10001
for i in range(int(sys.stdin.readline())):
    c[int(sys.stdin.readline())] += 1
for i in range(10001):
    for _ in range(c[i]):
        sys.stdout.write(str(i) + "\n")