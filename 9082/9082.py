import sys
def input():
    return sys.stdin.readline().rstrip()
def in_range(x):
    if 0 <= x < N: return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int, input()))
    land = list(input())
    mine = 0
    for i in range(N):
        if land[i] == '*':
            for j in range(i-1,i+2):
                if in_range(j):
                    num[j] -= 1
            mine += 1
    for i in range(3,1,-1):
        for j in range(N):
            cnt = 0
            if num[j] == i:
                for k in range(j-1,j+2,2):
                    if in_range(k) and num[k]:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt >= 2:
                    mine += 1
                    for k in range(j-1,j+2):
                        num[k] -= 1
    s = sum(num)
    mine += s//3 + (s%3!=0)
    print(mine)