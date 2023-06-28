import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n, *s = map(int, sys.stdin.readline().rstrip().split())
    print(f"{round(len(list(filter(lambda x:x>sum(s)/n, s)))*100/n, 3):.3f}%")