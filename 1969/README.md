# 백준 1969번 문제
https://www.acmicpc.net/problem/1969
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2021.01.16
---

### 접근 방식
- d와 hd는 Hamming Distance가 최소인 DNA 문자열과 그 값을 저장할 변수
- 각 자리의 A, T, C, G 수를 딕셔너리 DNA에 저장후 가장 많은 글자의 수를 n에서 빼서 그 자리의 Hamming Distance의 합의 최솟값을 구함
- 단, (글자의수,글자) 쌍들을 글자의 수는 오름차순, 글자는 아스키코드값의 내림차순으로 정렬하여 같은 Hamming Distance 값의 합이 나온 경우 사전순으로 더 앞에 있는 글자를 d에 더함
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 76ms
```Python
import sys
I = sys.stdin.readline
n, m = map(int,I().split())
d, hd = "", 0 #각각 Hamming Distance가 최소인 DNA 문자열과 그 값
D = [I().rstrip('\n') for _ in range(n)]
for i in range(m):
    DNA = {'A':0, 'T':0, 'C':0, 'G':0}
    for j in range(n):
        DNA[D[j][i]] += 1
    dna = []
    for j in DNA.keys():
        dna.append([DNA[j],j])
    dna.sort(reverse=True, key= lambda x: (x[0], -ord(x[1])))
    d += dna[0][1]
    hd += n-dna[0][0]
print(d)
print(hd)
```