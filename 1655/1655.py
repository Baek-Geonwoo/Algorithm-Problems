import sys
from heapq import *
S = []
B = []
def input():
    return int(sys.stdin.readline())
N = input()
for _ in range(N):
    if len(S) == len(B):
        heappush(S,-input())
    else:
        heappush(B,input())
    if len(B) != 0 and -S[0] > B[0]:
        b = -heappop(S)
        s = -heappop(B)
        heappush(S,s)
        heappush(B,b)
    print(-S[0])