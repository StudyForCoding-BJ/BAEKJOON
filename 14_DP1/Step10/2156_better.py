#BOJ 2156
#30864KB, 80ms
#1차원 배열로 줄임
import sys
num = int(input())
wine = [0]
for i in range(num):
    wine.append(int(sys.stdin.readline().strip()))

dp = [0]*(num+1)

for i in range(1, num+1):
    if i == 1:
        dp[i] = wine[i]
    elif i == 2:
        dp[i] = wine[i-1]+wine[i]
    else:
        dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
print(max(dp))