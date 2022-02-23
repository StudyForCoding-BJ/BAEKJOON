# 68ms
# 30864KB

import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

arr.sort()
gcd = arr[-1] - arr[0]

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a  

# 두 수의 차
val = []
for i in range(N - 1):
    val.append(abs(arr[i] - arr[i+1]))

# val들의 최대공약수
gcd = val[0]
for i in range(N - 2):
    gcd = GCD(gcd, val[i+1])
        
result = [gcd]
# 최대공약수의 약수
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)

result = list(set(result))
result.sort()
print(*result)