import sys
def check(S):
    vow = 0
    for v in "aeiou":
        if v in S: vow += 1
    if len(S)-vow >= 2 and vow >= 1: return True
    return False
def solution(i,S):
    if len(S) == L:
        if check(S):
            print(S)
        return
    if i == C: return
    solution(i+1,S+A[i])
    solution(i+1,S)

L, C, *A = sys.stdin.read().split()
L, C = int(L), int(C)
A.sort()
solution(0,"")