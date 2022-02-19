import sys
I = sys.stdin.readline
N, C = map(int, I().split())
H = [int(I()) for _ in range(N)]
H.sort()
low, high = 1, H[-1] - H[0]
ans = 0
while low <= high:
    m = (low+high)//2
    curr = H[0]
    cnt = 1
    for i in range(1,N):
        if H[i] >= curr + m:
            cnt += 1
            curr = H[i]
    if cnt >= C:
        ans = m
        low = m+1
    else:
        high = m-1
print(ans)