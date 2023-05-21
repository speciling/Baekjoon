from sys import stdin
from collections import Counter
import heapq
input = stdin.readline


for tc in range(int(input())):
    counter = Counter()
    min_h = []
    max_h = []
    for _ in range(int(input())):
        c, n = input().split()
        if c == "I":
            heapq.heappush(min_h, int(n))
            heapq.heappush(max_h, -int(n))
            counter[int(n)] += 1
        else:
            if n == "1":
                while max_h and counter[-max_h[0]] == 0:
                    heapq.heappop(max_h)
                if max_h:
                    counter[-(heapq.heappop(max_h))] -= 1
            else:
                while min_h and counter[min_h[0]] == 0:
                    heapq.heappop(min_h)
                if min_h:
                    counter[heapq.heappop(min_h)] -= 1

    while max_h and counter[-max_h[0]] == 0:
        heapq.heappop(max_h)
    while min_h and counter[min_h[0]] == 0:
        heapq.heappop(min_h)

    print(f"{-heapq.heappop(max_h)} {heapq.heappop(min_h)}" if max_h else "EMPTY")

