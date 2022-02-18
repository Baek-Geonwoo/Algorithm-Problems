# 백준 11728번 배열 합치기
https://www.acmicpc.net/problem/11728
---

### 문제 해결 날짜
- 2021.02.19
---

### 풀이1 코드 설명
- a, b는 각각 A, B의 인덱스를 가리키는 포인터
- a, b가 0으로 시작해서 a가 N이 되거나 b가 M이 될 때까지 다음을 반복한다.
    * ```A[a]>B[b]이면 A[a]를 출력하고 a+=1```
    * ```A[a]<=B[b]이면 B[b]를 출력하고 b+=1```
- while 루프를 빠져나오면 ```i가 a부터 N-1까지, b부터 M-1까지 A[i], B[i]를 출력한다.```(while 루프를 빠져나왔으므로 a=N 또는 b=M이기 때문에 두 반복문 중 하나는 실행되지 않는다.)
- 시간복잡도 O(N+M)
---

### 풀이1 소스코드
- 메모리 : 184432KB
- 시간 : 2328ms
```Python
import sys
I = sys.stdin.readline
N, M = map(int, I().split())
A = [int(e) for e in I().split()]
B = [int(e) for e in I().split()]
a, b = 0, 0
while a < N and b < M:
    if A[a] < B[b]:
        print(A[a], end=" ")
        a += 1
    else:
        print(B[b], end=" ")
        b += 1
for i in range(a,N):
    print(A[i], end=" ")
for i in range(b,M):
    print(B[i], end=" ")
```
---

### 풀이2 코드 설명
- N, M은 입력은 받으나 사용하지 않으므로 readline으로 한줄을 입력받는다.
- stdin.read()로 A, B를 받아 split으로 나눠 정수 기준으로 정렬하여 join을 사용해 출력한다.(정수로 정렬하지 않으면 "100">"19"같은 경우가 거짓이 되기 때문에 올바르게 정렬되지 않는다.)
- 시간복잡도가 풀이1보다 크지만, 시간은 오히려 적게 걸린다. 대신 메모리를 1.5배 정도 더 사용하는데 sorted함수 사용과정에서 메모리가 사용되는 것 같다.
- 메모리를 1.5배 사용하는 대신 시간을 3.5배 줄였다.
- 시간복잡도 O((N+M)log(N+M))
---

### 풀이2 소스코드
- 메모리 : 282908KB
- 시간 : 660ms
```Python
import sys
sys.stdin.readline()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))
```