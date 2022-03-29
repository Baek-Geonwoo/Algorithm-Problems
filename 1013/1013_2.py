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

def wave(i, n):
    if i == len(S):
        return n in (2,6,7)
    if dfa[n][int(S[i])] != None:
        return wave(i+1,dfa[n][int(S[i])])

for _ in range(int(I())):
    S = I().strip()
    print('YES') if wave(0,0) else print('NO')