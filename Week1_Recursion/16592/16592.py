from math import ceil
def sol(n,pos): # 1부터 n까지 0으로 끝나는 수 중 문제 조건 상 홀수 개수 구하는 함수
    # pos는 가장 큰 자리수의 0의 위치 1이면 1의자리수 2면 10의자리수
    if pos == len(n):
        return
    global odd
    odd += ceil(int(n[:-pos])/2)
    sol(n,pos+1)

A, B = map(int,input().split())
odd = 0 # 0으로 끝나는홀수번호판의 개수
sol(str(A),1)
oddA = ceil(A/2) + odd
evenA = A//2 - odd
odd = 0
sol(str(B),1)
oddB = ceil(B/2) + odd
evenB = B//2 - odd
odd = oddB-oddA
even = evenB-evenA
#A를 포함한 범위이므로 A를 포함시키기 위해서
if int(str(A).replace("0","")[-1])%2:
    odd += 1
else:
    even += 1
print(odd, even)