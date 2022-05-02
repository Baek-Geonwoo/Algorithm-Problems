import sys
N, C, *W = map(int, sys.stdin.read().split())
check = [0]*100000001
for w in W:
    check[w] = 1
if check[C]:
    print(1)
    sys.exit()
for i in range(N):
    for j in range(i+1,N):
        if W[i] + W[j] == C:
            print(1)
            sys.exit()
        elif W[i] + W[j] < C:
            remain = C - W[i] - W[j]
            if check[remain] and remain not in (W[i], W[j]):
                print(1)
                sys.exit()
print(0)