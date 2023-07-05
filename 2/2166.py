import sys
input = sys.stdin.readline

n = int(input())
dot = tuple(map(int, input().rstrip().split()))
vectors = [tuple(a-b for a,b in zip(map(int, input().rstrip().split()), dot)) for _ in range(n-1)]
total = 0
for i in range(n-2):
    v1, v2 = vectors[i], vectors[i+1]
    s = v1[0]*v2[1] - v1[1]*v2[0]
    total += s

print(round(abs(total)/2, 1))