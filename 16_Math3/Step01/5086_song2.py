#64ms
#30860KB
#while 무한루프문에서 입력받자마자 함수실행
import sys
    
def relation(m, n):
    if m < n:
        if n % m == 0:
            print("factor")
            return
    else:
        if m % n == 0:
            print("multiple")
            return
    print("neither")
    return

while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    relation(a, b)