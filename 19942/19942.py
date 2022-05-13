import sys
from itertools import combinations
def v_sum(V, l=0, r=3, C=[]):
    ret = [0]*(r+1)
    if not C:
        for v in V:
            for i in range(l,r+1):
                ret[i] += v[i]
        return ret
    else:
        for c in C:
            for i in range(l,r+1):
                ret[i] += V[c][i]
        return ret
def v_sub(V, W):
    return [v-w for v, w in zip(V,W)]
def v_boolean(V):
    return sum([v>=0 for v in V])
    
input = sys.stdin.readline
N = int(input())
m = list(map(int, input().split()))
I = [list(map(int, input().split())) for _ in range(N)]
if v_boolean(v_sub(v_sum(I),m))!=4:
    print(-1)
else:
    ans = 500*N
    ans_lst = []
    for i in range(1,N+1):
        for c in list(combinations(range(N), i)):
            if v_boolean(v_sub(v_sum(I,0,3,c),m))==4:
                cost = v_sum(I,4,4,c)[4]
                if cost < ans:
                    ans = cost
                    ans_lst = list(c)
                elif cost == ans:
                    if ans_lst > list(c):
                        ans_lst = list(c)
    print(ans)
    print(*v_sub(ans_lst,[-1]*len(ans_lst)))