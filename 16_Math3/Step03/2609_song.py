# 유클리드 호제법
# 76ms
# 30864KB

A, B = map(int, input().split())
a, b = A, B

while 1:
    if a % b == 0:
        gcd = b
        lmc = gcd * (A//gcd) * (B//gcd)
        print(gcd)
        print(lmc)
        break
    a, b = b, a % b
    
    
    