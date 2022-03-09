import sys
def dfs(idx, e, s):
    global ans
    if idx >= N:
        if idx == N:
            ans = min(ans, e)
        return
    if not s:
        dfs(idx+3,e+K,1)
    dfs(idx+1,e+S[idx][0],s)
    dfs(idx+2,e+S[idx][1],s)
I = sys.stdin.readline
N = int(I())
S = [0] + [tuple(map(int,I().split())) for _ in range(N-1)]
K = int(I())
ans = 5000*N
dfs(1,0,0)
print(ans)