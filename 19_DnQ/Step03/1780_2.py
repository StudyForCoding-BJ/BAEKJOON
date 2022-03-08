#BOJ 1780 _ 2
#3312ms
#값 dictionary화, n=1일 때의 조건문으로 return
import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
d = {-1:0, 0:0, 1:0}

def check(a: int, b: int, n: int):
    num = paper[a][b]
    if n == 1:
        d[num] += 1
        return
    for i in range(a, a+n):
        for  j in range(b, b+n):
            if num != paper[i][j]:
                check(a, b, n//3)
                check(a, b+(n//3), n//3)
                check(a, b+(n*2//3), n//3)
                check(a+(n//3), b, n//3)
                check(a+(n//3), b+(n//3), n//3)
                check(a+(n//3), b+(n*2//3), n//3)
                check(a+(n*2//3), b, n//3)
                check(a+(n*2//3), b+(n//3), n//3)
                check(a+(n*2//3), b+(n*2//3), n//3)
                return
    d[num] += 1
check(0, 0, n)
for i in d:
    print(d[i])