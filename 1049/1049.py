import sys
I = sys.stdin.readline
N, M = map(int, I().split())
S = [list(map(int, I().split())) for _ in range(M)]
Set, EA = 1000*6, 1000
for s, e in S:
    Set = min(Set, s)
    EA = min(EA, e)
print(min(Set*(N//6+1), Set*(N//6) + EA*(N%6), EA*N))