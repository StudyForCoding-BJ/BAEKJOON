#BOJ 1780 _ 4
#No dict, if로 return
#3380ms
#딕셔너리까지 합한 버전과 큰 차이는 나지 않지만(68ms 차이) 딕셔너리가 메모리를 잡아먹는 것도 아니고 딕셔너리를 쓰면 코드가 더 간결해짐
#Base case를 return 해 주는 처리가 최적화에 좋음
import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
neg, zero, pos = 0, 0, 0

def check(a: int, b: int, n: int):
    global neg, zero, pos
    num = paper[a][b]
    if n == 1:
        if num == -1:
            neg += 1
            return
        elif num == 0:
            zero += 1
            return
        else:
            pos += 1
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
    if num == -1:
        neg += 1
    elif num == 0:
        zero += 1
    else:
        pos += 1
check(0, 0, n)
print(neg, zero, pos, sep='\n')