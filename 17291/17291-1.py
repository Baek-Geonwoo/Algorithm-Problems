import sys
n = int(sys.stdin.readline())
P = [0]*21 #P[i]는 i년에 탄생한 벌레의 수
P[1] = 1
P[2] = 1
P[3] = 2
for i in range(4,n+1):
    born = 0
    if i%2:
        for j in range(i-3,i):
            born += P[j]
    else:
        for j in range(i-4,i):
            born += P[j]
    P[i] = born
survived = 0 #생존 개체의 수
if n <= 3:
    for i in range(1,n+1):
        survived += P[i]
else:
    if n%2:
        for i in range(n-3,n+1):
            survived += P[i]
    else:
        for i in range(n-2,n+1):
            survived += P[i]
print(survived)