#BOJ 2156
#31880KB, 92ms
#2차원 배열 활용
import sys
num = int(input())
wine = [0]
for i in range(num):
    wine.append(int(sys.stdin.readline().strip()))

dp = [[0]*3 for i in range(num+1)]

for i in range(1, num+1):
    for j in range(3):
        if i == 1:
            if j == 0 or j == 2:
                dp[i][j] = 0
            elif j == 1:
                dp[i][j] = wine[i]
        else:
            if j == 0:
                dp[i][j] = max(dp[i-1])
            else:
                dp[i][j] = dp[i-1][j-1] + wine[i]
print(max(map(max, dp)))