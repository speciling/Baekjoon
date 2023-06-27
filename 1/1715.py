import sys
import heapq
input = sys.stdin.readline

cards = [int(input()) for _ in range(int(input()))]
heapq.heapify(cards)

ans = 0
for _ in range(len(cards)-1):
    n = heapq.heappop(cards)+heapq.heappop(cards)
    heapq.heappush(cards, n)
    ans += n
print(ans)