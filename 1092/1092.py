import sys
I = sys.stdin.readline
N = int(I())
C = [int(e) for e in I().split()]
M = int(I())
B = [int(e) for e in I().split()]
if max(C) < max(B):
    print(-1)
else:
    C.sort(reverse=True)
    B.sort(reverse=True)
    pos = [0]*N
    moved = [0]*M
    cnt = 0
    ans = 0
    while cnt<M:
        for i in range(N):
            while pos[i] < M:
                if not moved[pos[i]] and B[pos[i]] <= C[i]:
                    moved[pos[i]] = 1
                    pos[i] += 1
                    cnt += 1
                    break
                pos[i] += 1
        ans += 1
    print(ans)