import sys
I = sys.stdin.readline
N, M = map(int, I().split())
P = [int(I()) for _ in range(M)]
P.sort()
price, profit = 0, 0
for i in range(M):
    curr = P[i]*min(N,M-i)
    if curr > profit:
        profit = curr
        price = P[i]
print(price, profit)