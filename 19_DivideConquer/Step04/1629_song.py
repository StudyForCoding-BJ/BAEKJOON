# BOJ 1629
# 72ms
# 30864KB

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

result = 1
def multi(n):
    
    global result
    
    # Base Case
    if n == 1:
        result = A % C
        return result 
        
    # Recursion Case
    else:
        # Divide
        if n % 2 != 0:
            n = n // 2
            temp = multi(n) % C
            # Combine
            result = temp * temp * multi(1)
        else:
            n = n // 2
            temp = multi(n) % C
            # Combine
            result = temp * temp
        return result

multi(B)
print(result % C)

