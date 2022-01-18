import sys
n = int(sys.stdin.readline())
d, l = 1, 0 #d, l은 각각 n=i일때 점으로 끝나는 경우의 수, 선으로 끝나는 경우의 수
i=1
while i<n:
    d, l = (d+l)%10, d%10
    i+=1
print((d+l)%10)