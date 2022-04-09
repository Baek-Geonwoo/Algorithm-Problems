import sys
import heapq
I = sys.stdin.readline
N = int(I())
H = []
for _ in range(N):
    a = int(I())
    if a == 0:
        if H:
            print(heapq.heappop(H)[1])
        else:
            print(0)
    else:
        heapq.heappush(H,(abs(a),a))