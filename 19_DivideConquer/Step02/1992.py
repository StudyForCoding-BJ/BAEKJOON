#BOJ 1992
import sys

n = int(input())
vid = []
vid = [sys.stdin.readline().strip() for i in range(n)]
res = ''

def check(a:int, b:int, n:int):
    global res
    for i in range(a,a+n):
        color = vid[i][b:b+n]
        if color == '0'*n and i == a+n-1:
            res += '0'
            return
        elif color == '1'*n and i == a+n-1:
            res += '1'
            return
        else:
            for j in range(i, a+n):
                if vid[j][b:b+n] != color or (color != '0'*n and color != '1'*n):
                    res += '('
                    check(a, b, n//2)
                    check(a, b+(n//2), n//2)
                    check(a+(n//2), b, n//2)
                    check(a+(n//2), b+(n//2), n//2)
                    res += ')'
                    return
check(0, 0, n)
print(res)