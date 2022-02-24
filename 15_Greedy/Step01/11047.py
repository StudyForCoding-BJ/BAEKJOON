#BOJ 11047
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline().strip()))
cnt = 0
i = n-1
while i >= 0 and k != 0:
    num = k//coins[i]
    if num > 0:
        cnt += num
        k -= coins[i]*num
    i -= 1
