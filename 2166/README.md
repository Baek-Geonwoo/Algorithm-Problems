# 백준 2166번 다각형의 면적
https://www.acmicpc.net/problem/2166
---

### 문제 해결 날짜
- 2021.03.06
---

### 코드 설명
- N각형은 N-2개의 삼각형으로 나눌 수 있다.
- 처음 입력받은 점을 s라 하고 그 좌표를 sx, sy라 한다. 이 점을 공유하는 삼각형들로 N각형을 N-2개의 삼각형으로 자른다.
- 두번째로 입력받은 점을 p라하고, 그 다음부터 다음을 N-2번 반복한다.
- 세번째 이후부터 입력받은 점을 c라하고, s, p, c로 이루어진 삼각형의 넓이를 외적을 이용하여 구하여 ans에 더한 후 p를 c로 초기화한다.
- 오목한 다각형인 경우도 있을 수 있으므로 외적으로 구해야 한다.
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 84ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
ans = 0
sx, sy = map(int, I().split())
px, py = map(int, I().split())
for i in range(N-2):
    cx, cy = map(int, I().split())
    ans += ((px-sx)*(cy-sy)-(py-sy)*(cx-sx))/2
    px, py = cx, cy
print("%.1f" %abs(ans))
```