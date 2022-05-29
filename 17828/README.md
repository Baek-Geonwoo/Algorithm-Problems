# 백준 17828번 문자열 화폐
https://www.acmicpc.net/problem/17828
---

### 문제 해결 날짜
- 2022.05.29
---

### 코드 설명
- N > X 또는 X > N * 26이면 해당하는 문자열이 없는 것이므로 !을 출력한다.
- 사전 순으로 가장 앞서려면 사전 순으로 뒤에 있는 알파벳이 문자열의 오른쪽에 있어야 하므로 X//25 만큼 ans의 오른쪽에 추가하고 X에서 `X//25*25`를 뺀다.
- `ans = "A"*(N-(X!=0)) + chr(65+X%25)*(X!=0) + ans`
---

### 소스코드
- 메모리 : 40604 KB
- 시간 : 80 ms
```Python
import sys
N, X = map(int, sys.stdin.readline().split())
if N > X or X > N * 26:
    print("!")
else:
    X -= N
    ans = X // 25 * "Z"
    N -= X // 25
    X -= X // 25 * 25
    ans = "A"*(N-(X!=0)) + chr(65+X%25)*(X!=0) + ans
    print(ans)
```