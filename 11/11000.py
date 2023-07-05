import sys
import heapq
lectures = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline()))]
lectures.sort()
rooms = [0]
for s, t in lectures:
    if s >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, t)

print(len(rooms))
