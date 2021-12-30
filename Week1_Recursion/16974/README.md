# 백준 16974번 문제
https://www.acmicpc.net/problem/16974
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버II
- 2021.12.30
---

### 접근 방식
- DP로 1~50까지의 총 버거 장수와 패티 수를 각각 B, P에 저장 B[n]=2*B[n-1]+3, P[n] = 2*P[n-1]+1
- n이 0이면 x는 0또는 1이고 결과는 x에 비례 (아래부터 ||사이가 범위에 포함되는것 중간에 |가 있으면 중간 또는 전체인 경우)
- B[n]-n <= x이면 버거의 위는 버거 번이 연속으로 n개이상 나오므로 P[n] (|B(|n-1)P(n-1)B)
- n >= x이면 버거의 밑은 버거 번이 연속으로 n개이상 나오므로 0 (B(n-1)P(n-1|)B|)
- x <= B[n-1]+1이면 가장 밑에 레벨n버거의 번이 있으므로 solve(n-1,x-1) (B(n-1)P|(n-1)B|)
- x == 1+B[n-1]+1이면 밑에서부터 레벨n버거에서 추가된 패티까지만 포함이므로 1+P[n-1] (B(n-1)|P(n-1)B|)
-x > 1+B[n-1]+1이면 밑에서부터 위쪽 레벨 n-1버거 일부를 포함하므로 solve(n-1,x-1-B[n-1]-1)+1+P[n-1] (B(n-1|)P(n-1)B|)
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 64ms
```Python
def solve(n,x):
    if n == 0:
        return max(n,x)
    if B[n]-n<=x: #레벨 n버거의 맨위는 n개 이상의 버거 번이 있으므로
        return P[n]
    if n>=x: #레벨 n버거의 맨 아래는 n개 이상의 버거 번이 있으므로
        return 0
    if x <= B[n-1]+1:
        return solve(n-1,x-1)
    elif x == 1+B[n-1]+1:
        return 1+P[n-1]
    elif x > 1+B[n-1]+1:
        return solve(n-1,x-1-B[n-1]-1)+1+P[n-1]

n, x = map(int,input().split())
P = [0]*51
B = [0]*51
P[0], B[0] = 1, 1
for i in range(1,n+1):
    P[i] = P[i-1] + 1 + P[i-1]
    B[i] = 1+ B[i-1] + 1 + B[i-1] + 1
print(solve(n,x))
```