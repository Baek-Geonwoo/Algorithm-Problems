import sys
from itertools import combinations as comb
input = sys.stdin.readline
N, M = map(int, input().split())
R = [list(map(int,list(input().rstrip()))) for _ in range(N)]
ans = 0
if M >= 3:
    for c in comb(range(1,M), 2):
        rge = [0]+list(c)+[M]
        s = [0]*3
        for n in range(3):
            for i in range(N):
                for j in range(*rge[n:n+2]):
                    s[n] += R[i][j]
        ans = max(ans, s[0]*s[1]*s[2])
if N >= 3:
    for c in comb(range(1,N), 2):
        rge = [0]+list(c)+[N]
        s = [0]*3
        for n in range(3):
            for i in range(M):
                for j in range(*rge[n:n+2]):
                    s[n] += R[j][i]
        ans = max(ans, s[0]*s[1]*s[2])
if N >= 2 and M >= 2:
    for n in range(1,N):
        for m in range(1,M):
            s = [0]*4
            rgeN = [0,n,N]
            rgeM = [0,m,M]
            for nn in range(2):
                for mm in range(2):
                    for i in range(*rgeN[nn:nn+2]):
                        for j in range(*rgeM[mm:mm+2]):
                            s[nn*2+mm] += R[i][j]
            ans = max(ans, (s[0]+s[1])*s[2]*s[3])
            ans = max(ans, s[0]*(s[1]+s[3])*s[2])
            ans = max(ans, s[0]*s[1]*(s[2]+s[3]))
            ans = max(ans, (s[0]+s[2])*s[1]*s[3])
print(ans)