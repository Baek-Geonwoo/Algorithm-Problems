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