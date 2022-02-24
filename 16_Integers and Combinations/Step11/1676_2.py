#BOJ 1676 _ 2
#문자열, 32976KB, 76ms
#1676_1을 다시 그대로 채점한 결과 76ms였으므로 서버 상의 시간단축
from math import factorial
a = str(factorial(int(input())))
a = a[::-1]
cnt = 0
while a[0] == '0':
    cnt += 1
    a = a[1:]
print(cnt)