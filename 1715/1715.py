import sys, heapq
N, *heap = map(int, sys.stdin.read().split())
heapq.heapify(heap)
ans = 0
for _ in range(N-1):
    compare = heapq.heappop(heap) + heapq.heappop(heap)
    ans += compare
    heapq.heappush(heap, compare)
print(ans)