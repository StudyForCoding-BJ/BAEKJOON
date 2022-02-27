#BOJ 3036
import math
n = int(input())
wheel = list(map(int, input().split()))
for i in range(1, n):
    g = math.gcd(wheel[0], wheel[i])
    s = wheel[0]//g
    m = wheel[i]//g
    print(f"{s}/{m}")