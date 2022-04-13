import sys
T, W, *A = map(int, sys.stdin.read().split())
# P[t][w]는 t+1초까지 w번 움직여 받을 수 있는 자두의 최대 개수
P = [[0]*(W+1) for _ in range(T+1)]
for t in range(1,T+1):
    P[t][0] = P[t-1][0] + int(A[t-1] == 1)
    for w in range(1,W+1):
        P[t][w] = max(P[t-1][w],P[t-1][w-1]) + int(A[t-1]%2 == (w+1)%2)
print(max(P[-1]))