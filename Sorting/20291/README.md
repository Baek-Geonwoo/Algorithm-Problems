# 백준 20291번 문제
https://www.acmicpc.net/problem/20291
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버III
- 2021.01.12
---

### 접근 방식
- 딕셔너리 E에 확장자:그 확장자가 나온 횟수 쌍을 저장
- 입력된 파일 이름에서 확장자만 필요하므로 split으로 파일 이름에서 .뒤쪽의 확장자만 e에 저장
- e가 나왔으므로 E[e] += 1을 하는데 E에 e가 key로 없으면 오류가 발생하므로 try를 사용하여 예외상황이 발생하면 E에 e를 key로 등록
- E의 key들을 사전순으로 정렬하여 확장자 나온횟수를 출력
---

### 소스코드
- 메모리 : 40960KB
- 시간 : 248ms
```Python
import sys
I = sys.stdin.readline
n = int(I())
E = {}
for i in range(n):
    e = I().strip('\n').split(".")[1]
    try:
        E[e] += 1
    except:
        E[e] = 1
for e in sorted(E.keys()):
    print(e,E[e])
```