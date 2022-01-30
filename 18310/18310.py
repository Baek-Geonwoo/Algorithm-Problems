import sys
I = sys.stdin.readline
N = int(I())
H = [int(e) for e in I().split()]
H.sort()
print(H)
print(H[N//2-(N%2==0)])