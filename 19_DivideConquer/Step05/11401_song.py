# BOJ 11401
# 1244ms
# 30864KB

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
P = 1000000007

# 재귀로 구현하면 런타임에러 (RecursionError)
# 팩토리얼 곱할 때마다 P로 나눠줘야 시간초과 해결
def factorial(n):
    temp  = 1
    for i in range(2, n+1):
        temp *= i
        temp %= P
    return temp 

# 거듭제곱    
result = 1
def power(n):
    
    global result 
    
    if n == 1:
        result = A % P
        return result
    else:
        if n % 2 != 0:
            n = n // 2
            temp = power(n) % P
            result = temp * temp * power(1)
        else:
            n = n // 2
            temp = power(n) % P
            result = temp * temp
        return result

A = factorial(K) * factorial(N-K) % P
final = (factorial(N) * power(P-2)) % P
print(final)

'''
페르마의 소정리
https://to06109.tistory.com/28
'''
