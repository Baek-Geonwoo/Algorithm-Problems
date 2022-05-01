import sys
G = int(sys.stdin.readline())
flag = 1
for n in range(int(G**0.5),0,-1):
    if G%n==0 and (n+G//n)%2 == 0 and n!=G//n:
        print(n,G//n,(n+G//n)//2)
        flag = 0
if flag: print(-1)