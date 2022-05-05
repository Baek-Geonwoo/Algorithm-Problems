# 백준 6576번 쿼드 트리
https://www.acmicpc.net/problem/6576
---

### 문제 해결 날짜
- 2022.05.05
---

### 코드 설명
- 쿼드 트리 코드를 해체한 후 nxn 2차원 리스트 Q에 B인 곳만 1로 초기화해서 8비트로 재구성한다.
---

### 소스코드
- 메모리 : 32156 KB
- 시간 : 312 ms
```Python
def solve(x,y,size):
    global idx
    if S[idx] == "Q":
        size //= 2
        idx += 1
        solve(x,y,size)
        solve(x,y+size,size)
        solve(x+size,y,size)
        solve(x+size,y+size,size)
    else:
        if S[idx] == "B":
            for i in range(x,x+size):
                for j in range(y,y+size):
                    Q[i][j] = 1
        idx += 1
n = int(input())
S = input()
Q = [[0]*n for i in range(n)]
idx = 0
solve(0,0,n)
print("#define quadtree_width", n)
print("#define quadtree_height", n)
print("static char quadtree_bits[] = {")
for i in range(n):
    for j in range(n//8):
        b = 0 #비트값의 지수 2^b
        bit = 0 #비트값
        for k in range(j*8,(j+1)*8):
            bit += Q[i][k]*2**b
            b += 1
        print('{:#04x}'.format(bit),end=",")
    print()
print("};")
```
---

### 오답 노트
- 틀렸습니다.
- 문제에 완벽한 쿼드 트리로만 구성되어있다고 해서 QBBWB같은 구조가 반복되는 구조인줄 알았다.

### 오답 코드
```Python
def solve(S,p,x,y):
    if S[0] == "Q":
        n = len(S)-1
        solve(S[1:n//4+1],p//2,x,y)
        solve(S[n//4+1:2*n//4+1],p//2,x,y+p//2)
        solve(S[2*n//4+1:3*n//4+1],p//2,x+p//2,y)
        solve(S[3*n//4+1:4*n//4+1],p//2,x+p//2,y+p//2)
    else:
        if S[0] == "B":
            for i in range(x,x+p):
                for j in range(y,y+p):
                    Q[i][j] = 1
        else:
            for i in range(x,x+p):
                for j in range(y,y+p):
                    Q[i][j] = 0

n = int(input())
S = input()
Q = [[0]*n for i in range(n)]
solve(S,n,0,0)
print("#define quadtree_width", n)
print("#define quadtree_height", n)
print("static char quadtree_bits[] = {")
for i in range(n):
    for j in range(n//8):
        b = 0 #비트값의 지수 2^b
        bit = 0 #비트값
        for k in range(j*8,(j+1)*8):
            bit += Q[i][k]*2**b
            b += 1
        print(hex(bit),end=",")
    print()
print("};")
```