import sys
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
F = [list(I().strip()) for _ in range(N)]
ans = 0
for x in range(N):
    for y in range(M):
        X = x-int(F[x][y]=='|')
        Y = y-int(F[x][y]=='-')
        if in_range(X,Y):
            if F[x][y] != F[X][Y]:
                ans += 1
        else:
            ans += 1
print(ans)