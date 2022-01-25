import sys
N, M = map(int, sys.stdin.readline().split())
if N == 1:
    ans = 1
elif N==2:
    ans = min((M-1)//2+1,4)
elif M<7:
    ans = min(M,4)
else:
    ans = M-7+5
print(ans)