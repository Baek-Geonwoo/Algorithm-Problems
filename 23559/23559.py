from sys import stdin
I = stdin.readline
N, X = map(int, I().split())
M = [list(map(int, I().split())) for _ in range(N)]
M.sort(key = lambda x: -(x[0]-x[1]))
X -= 1000*N
ans = 0
for a, b in M:
    if a > b and X>=4000:
        ans += a
        X -= 4000
    else:
        ans += b
print(ans)