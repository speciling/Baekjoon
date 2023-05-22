from sys import stdin
import heapq
from collections import defaultdict
input = stdin.readline

# 절댓값 전부 그대로 넣고 음수 갯수 따로 카운트하기
heap = []
negative_count = defaultdict(int)
for _ in range(int(input())):
    n = int(input())
    if n:
        if n > 0:
            heapq.heappush(heap, n)
        elif n < 0:
            heapq.heappush(heap, -n)
            negative_count[n] += 1
    else:
        if heap:
            minNum = heapq.heappop(heap)
            if negative_count[-minNum]:
                minNum *= -1
                negative_count[minNum] -= 1
            print(minNum)
        else:
            print(0)