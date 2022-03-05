import sys
I = sys.stdin.readline
N = int(I())
P = [tuple(map(int, I().split())) for _ in range(N)]
h_index, h = [], 0
P.sort()
for i in range(N):
    if h < P[i][1]:
        h_index = []
        h_index.append(i)
        h = P[i][1]
    elif h == P[i][1]:
        h_index.append(i)
ans = h*(P[h_index[-1]][0]-P[h_index[0]][0]+1)
prev_L, prev = P[0][0], P[0][1]
for i in range(1,h_index[0]+1):
    if prev < P[i][1]:
        ans += prev*(P[i][0]-prev_L)
        prev_L, prev = P[i][0], P[i][1]
prev_L, prev = P[N-1][0], P[N-1][1]
for i in range(N-2,h_index[-1]-1,-1):
    if prev < P[i][1]:
        ans += prev*(prev_L-P[i][0])
        prev_L, prev = P[i][0], P[i][1]
print(ans)