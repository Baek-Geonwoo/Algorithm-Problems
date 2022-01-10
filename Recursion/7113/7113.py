def sol(n, m, cnt):
    if n*m == 0:
        print(cnt)
        return
    n, m = max(n,m), min(n,m)
    cnt += n//m
    n -= n//m*m
    sol(n,m,cnt)

n,m = map(int,input().split())
sol(n,m,0)