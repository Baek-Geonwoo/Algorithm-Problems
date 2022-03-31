import sys
I = sys.stdin.readline
dfa = ((1,3),
    (None,2),
    (1,3),
    (4,None),
    (5,None),
    (5,6),
    (1,7),
    (8,7),
    (5,2)
)

def solve(i, n):
    if i == len(S):
        return n in (2,6,7)
    if dfa[n][int(S[i])] != None:
        return solve(i+1,dfa[n][int(S[i])])

S = sys.stdin.readline().strip()
print("SUBMARINE") if solve(0,0) else print("NOISE")