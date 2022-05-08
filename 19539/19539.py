import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))
if sum(H)%3 != 0:
    print('NO')
else:
    if sum([h//2 for h in H]) >= sum(H)//3:
        print('YES')
    else:
        print('NO')