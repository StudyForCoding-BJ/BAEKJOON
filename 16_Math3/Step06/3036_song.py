# 132ms
# 36696KB

from fractions import Fraction

N = int(input())
R = list(map(int, input().split()))

for i in range(1, N):
    if R[0] % R[i] == 0: # 나누어 떨어질 때
        print(R[0]//R[i], '/', 1, sep='')
    else:
        number = Fraction(R[0], R[i]) #기약분수
        numer = number.numerator # 분자
        denomi = number.denominator # 분모
        print(numer, '/', denomi, sep='')
