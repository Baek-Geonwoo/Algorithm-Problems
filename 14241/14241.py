import sys
I = sys.stdin.readline
n = int(I())
S = [int(e) for e in I().split()]
S.sort()
temp = S[0]
score = 0
for i in range(1,n):
    score += temp*S[i]
    temp += S[i]
print(score)