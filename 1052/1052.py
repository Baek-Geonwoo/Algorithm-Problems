import sys
N, K = map(int, sys.stdin.readline().split())
#이진수로 바꿨을 때 1의 수가 물병의 수
#그리디 기준: 이진수의 1의 개수가 K보다 클 때 작은 자리의 1부터 소거
buy = 0
B = format(N, 'b')
if B.count('1') <= K:
    print(buy)
else:
    i = 1
    while B.count('1') > K:
        if B[-i] == '1':
            B = format(int(B,2)+2**(i-1), 'b')
            buy += 2**(i-1)
        i += 1
    print(buy)