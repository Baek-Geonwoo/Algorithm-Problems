import sys
input = sys.stdin.readline
L = [int(e) for e in input().split()]

while L != [1,2,3,4,5]:
    for i in range(4):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
            print(*L)