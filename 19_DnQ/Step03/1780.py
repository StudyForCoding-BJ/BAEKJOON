#BOJ 1780
#5704ms
#서버 시간 단축이 있는지 확인하기 위해 재채점했으나 오히려 더 늘어남
import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
neg, zero, pos = 0, 0, 0

def check(a: int, b: int, n: int):
    global neg, zero, pos
    num = paper[a][b]
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
    if num == -1:
        neg += 1
    elif num == 0:
        zero += 1
    else:
        pos += 1
check(0, 0, n)
print(neg, zero, pos, sep='\n')