import sys
import heapq
I = sys.stdin.readline
N, K = map(int, I().split())
H = [(-int(ci), i) for ci, i in zip(I().split(), range(1,K+1))]
heapq.heapify(H)
if -H[0][0]*2 > N+1:
    print(-1)
else:
    prev = 0
    for _ in range(N):
        ci, i = heapq.heappop(H)
        if prev == i:
            cj, j = heapq.heappop(H)
            print(j, end=" ")
            heapq.heappush(H, (cj+1,j))
            heapq.heappush(H, (ci,i))
            prev = j
        else:
            print(i, end=" ")
            heapq.heappush(H, (ci+1,i))
            prev = i