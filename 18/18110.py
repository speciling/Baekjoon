import sys
input = sys.stdin.readline
r = lambda x:int(x)+(x-int(x) >= 0.5)

n = int(input())
m = r(n*0.15)
arr = sorted([int(input()) for _ in range(n)])
if m != 0:
    arr = arr[m:-m]
print(r(sum(arr)/len(arr)) if arr else 0)