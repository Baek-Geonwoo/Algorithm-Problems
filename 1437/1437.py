import sys
N = int(sys.stdin.readline())
if N <= 2:
    print(N)
else:
    print(3**(N//3-1) * max(3+N%3, 3*(N%3))%10007)