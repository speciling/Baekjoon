n = int(input())
p = list(map(int, input().split()))
p.sort()
print(sum([t*(n-i) for i, t in enumerate(p)]))