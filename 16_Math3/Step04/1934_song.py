# 72ms
# 30864KB
# readline으로 입력받는게 시간 2배 빠름

import sys

N = int(input())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    a, b = A, B
    if b > a:
        a, b = b, a
    while 1:
        if b == 0:
            break
        a, b = b, a % b
    GCD = a
    print(A * B // GCD)