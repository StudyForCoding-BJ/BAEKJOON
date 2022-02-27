#BOJ 1676
#사칙연산 사용, 32976KB, 80ms
#큰 숫자가 입력될 경우 시간이 오래걸릴 수 있을 것 같음
from math import factorial
a = factorial(int(input()))
cnt = 0
while a % 10 == 0:
    cnt += 1
    a = a//10
print(cnt)