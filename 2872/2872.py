import sys
I = sys.stdin.readline
N = int(I())
L = [int(I()) for _ in range(N)]
m = N
#오름차순 아닌 가장 큰 수
for i in range(N-1,-1,-1):
    if L[i] == m:
        m -= 1
print(m)