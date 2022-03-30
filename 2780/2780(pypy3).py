import sys
def in_range(x,y):
    if x == 3 and y == 0:
        return True
    elif 0<=x<3 and 0<=y<3:
        return True
    return False
T, *L = map(int, sys.stdin.read().split())
d = (-1,0), (1,0), (0,-1), (0,1)
for t in range(T):
    N = L[t]
    P = [[0]*10 for _ in range(N+1)] #P[i][j]는 j로 끝나는 i자리 비밀번호의 수
    P[1] = [1]*10
    K = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
    pos = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        0:(3,0)
        }
    for i in range(2,N+1):
        for j in range(10):
            x, y = pos[j]
            for dx,dy in d:
                nx, ny = x+dx, y+dy
                if in_range(nx,ny):
                    P[i][j] += P[i-1][K[nx][ny]]
            P[i][j] %= 1234567
    print(sum(P[N])%1234567)