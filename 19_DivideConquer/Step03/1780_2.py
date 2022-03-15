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

#1780_3   
#값 dictionary화, n=1일 때의 조건문으로 return 중 무엇이 시간 단축 키포인트인지 확인
#값 dictionary화 -> 5348ms
#Dictionary로 만드는 것도 시간 단축에 기여(약 400ms)를 하지만
#if로 n=1일 때의 return을 달아주는 게 큰 역할을 한 것으로 보임.
#1780_4에서 확인

#1780_4 
#No dict, if로 return
#3380ms
#딕셔너리까지 합한 버전과 큰 차이는 나지 않지만(68ms 차이) 딕셔너리가 메모리를 잡아먹는 것도 아니고 딕셔너리를 쓰면 코드가 더 간결해짐
#Base case를 return 해 주는 처리가 최적화에 좋음