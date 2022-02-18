# 68ms
# 30860KB

N = int(input())
R = list(map(int, input().split()))

def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

for i in range(1, N):
    gcd = find_gcd(R[0], R[i])
    print(R[0]//gcd, '/', R[i]//gcd, sep='')