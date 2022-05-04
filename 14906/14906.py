import sys
import re
def input():
    return sys.stdin.readline().strip()
def Slimp(S):
    if len(S)<2: return 0
    if S[:2] == 'AH' and len(S) == 2:
        return 1
    elif S[0] == 'A' and S[-1] == 'C':
        if S[1] == 'B':
            return Slimp(S[2:-1])
        else:
            return re.fullmatch('((D|E)F+)+G', S[1:-1])
    else: return 0
def SLURPY(S):
    slump = re.search('(((D|E)F+)+G)$', S)
    if slump:
        S = S[:slump.span()[0]]
    else: return 0
    return Slimp(S)

print("SLURPYS OUTPUT")
for _ in range(int(input())):
    if SLURPY(input()):
        print("YES")
    else:
        print("NO")
print("END OF OUTPUT")