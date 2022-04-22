import sys
input = sys.stdin.readline
def f(n):
    if n <= 1:
        return 1
    return n*f(n-1)
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    N, M = min(N, M), max(N, M)
    print(f(M)//(f(N)*f(M-N)))