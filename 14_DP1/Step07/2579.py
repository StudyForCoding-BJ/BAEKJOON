#BOJ 2579
import sys

num = int(input())
stairs = [0]
for i in range(num):
    stairs.append(int(sys.stdin.readline().strip()))

dp = [0]*(num+1)

for i in range(1, num+1):
    if i == 1:
        dp[i] = stairs[i]
    elif i == 2:
        dp[i] = dp[i-1]+stairs[i]
    else:
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[num])