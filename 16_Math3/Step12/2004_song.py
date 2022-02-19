# 시간초과

import sys
n, m = map(int, sys.stdin.readline().split())

up = 1
down = 1

if m > n // 2:
    m = n - m
    
for i in range(1, m + 1):
    up *= n - i + 1
    down *= i
comb = up // down % 1000000000

count = 0
while comb % 10 == 0:
    comb //= 10
    count += 1
    
print(count)
    