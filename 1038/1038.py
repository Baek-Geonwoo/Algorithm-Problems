import sys
def check(X, digit):
    global N
    if N <= 0: return
    if digit == 1:
        N -= 1
        if N == 0:
            print(X)
    else:
        for i in range(int(X[-1])):
            check(X+str(i), digit-1)
def backtrack(digit):
    global N
    if N <= 0: return
    for i in range(digit-1,10):
        check(str(i), digit)
N = int(sys.stdin.readline())+1
for i in range(1,11):
    backtrack(i)
if N>0:
    print(-1)