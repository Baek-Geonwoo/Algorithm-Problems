import sys
input = sys.stdin.readline
def B(x):
    return int(x,2)
T = int(input())
for _ in range(T):
    a, b = map(B,input().split())
    print(format(a+b,'b'))