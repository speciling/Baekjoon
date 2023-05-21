import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

heap = []
for i in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        print(str(heapq.heappop(heap))+"\n" if heap else '0\n')
