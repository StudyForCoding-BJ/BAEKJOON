#BOJ 1780 _ 3
#값 dictionary화, n=1일 때의 조건문으로 return 중 무엇이 시간 단축 키포인트인지 확인
#값 dictionary화 -> 5348ms
#Dictionary로 만드는 것도 시간 단축에 기여(약 400ms)를 하지만
#if로 n=1일 때의 return을 달아주는 게 큰 역할을 한 것으로 보임.
#1780_4에서 확인
import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
d = {-1:0, 0:0, 1:0}

def check(a: int, b: int, n: int):
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
    d[num] += 1
check(0, 0, n)
for i in d:
    print(d[i])