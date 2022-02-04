import sys
I = sys.stdin.readline
N = int(I())
D = [int(e) for e in I().split()]
if N == 1:
    print(sum(D)-max(D))
else:
    ans = 0
    #한 면만 보이는 주사위에 쓰인 수의 합의 최솟값
    ans += ((N-2)**2+4*(N-1)*(N-2))*min(D)
    #두 면이 보이는 주사위에 쓰인 수의 합의 최솟값
    m1 = max(D)*2
    for i in range(6):
        for j in range(6):
            if i==j or i+j == 5:
                continue
            m1 = min(m1,D[i]+D[j])
    ans += 4*(N-1+N-2)*m1
    #세 면이 보이는 주사위에 쓰인 수의 합의 최솟값
    m2 = max(D)*3
    for i in range(6):
        if i in [0,5]:
            stack = [1,2,4,3]
        elif i in [1,4]:
            stack = [2,0,3,5]
        else:
            stack = [4,0,1,5]
        for _ in range(4):
            m2 = min(m2,D[i]+D[stack[0]]+D[stack[1]])
            stack.append(stack.pop(0))
    ans += 4*m2
    print(ans)