import sys
I = sys.stdin.readline
n = int(I())
A = []
for _ in range(n):
    A.append(int(I()))
A.sort()
i = 0
score = 0
while i<n:
    if A[i]<0:
        try:
            if A[i+1]<0:
                score += A[i]*A[i+1]
                i += 2
            elif A[i+1]==0:
                break
            else:
                score += A[i]
                break
        except:
            score += A[i]
            break
    else:
        break
i = n-1
while 0<=i:
    if A[i]>0:
        try:
            if A[i-1]>0:
                score += max(A[i]*A[i-1],A[i]+A[i-1])
                i -= 2
            else:
                score += A[i]
                break
        except:
            score += A[i]
            break
    else:
        break
print(score)