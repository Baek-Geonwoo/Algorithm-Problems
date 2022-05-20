import sys
def input():
    return list(map(int,sys.stdin.readline().split()))
N, M = input()
P = input()
T = [input() for _ in range(N-1)]
C = [0]*N
for i in range(M-1):
    s = min(P[i], P[i+1])-1
    e = max(P[i], P[i+1])-1
    C[s] += 1
    C[e] -= 1
ans = 0
cnt = 0
for i in range(N-1):
    cnt += C[i]
    ans += cnt*T[i][0] if cnt*T[i][0] <= cnt*T[i][1]+T[i][2] else cnt*T[i][1]+T[i][2]
print(ans)