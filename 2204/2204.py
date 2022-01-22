import sys
I = sys.stdin.readline
while True:
    n = int(I())
    if n == 0:
        break
    w = I().rstrip('\n') #사전상 가장 앞서는 단어 저장
    for _ in range(n-1):
        curr = I().rstrip('\n')
        if w.lower() > curr.lower():
            w = curr
    print(w)