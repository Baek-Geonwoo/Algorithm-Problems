import sys
def broken_calc(n,i):
    global D, P, ans
    if n >= D:
        return
    if (n,i) in S:
        return
    S.add((n,i))
    if i == P:
        if n < D:
            ans = max(ans, n)
        return
    for x in range(2,10):
        broken_calc(n*x,i+1)
D, P = map(int, sys.stdin.readline().split())
D = 10**D
ans = 0
S = set()
broken_calc(1,0)
print(ans) if ans != 0 else print(-1)