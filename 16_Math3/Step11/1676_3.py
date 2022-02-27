#BOJ 1676 _ 3
#뒤집지 않고 뒤에서부터 처리한 문자열, 32976KB, 72ms
from math import factorial
a = str(factorial(int(input())))
cnt = 0
i = -1
while a[i] == '0':
    cnt += 1
    i -= 1
print(cnt)