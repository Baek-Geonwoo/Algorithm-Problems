import sys, heapq
I = sys.stdin.readline
N = int(I())
H = list(map(int,I().split()))
heapq.heapify(H)
for _ in range(N-1):
    A = map(int,I().split())
    for a in A:
        if H[0] < a:
            heapq.heappushpop(H,a)
print(H[0])