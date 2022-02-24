#BOJ 1676
#사칙연산 사용, 32976KB, 80ms
from math import factorial
a = factorial(int(input()))
cnt = 0
while a%10 == 0:
    cnt += 1
    a = a//10
print(cnt)