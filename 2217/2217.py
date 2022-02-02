import sys
I = sys.stdin.readline
N = int(I())
R = [int(I()) for _ in range(N)]
R.sort()
# 그리디 기준: 최대중량이 적은 로프부터 그 로프가 최대한 견딜 수 있게 w/k설정
W = 0
for i in range(N):
    W = max(W, R[i]*(N-i))
print(W)