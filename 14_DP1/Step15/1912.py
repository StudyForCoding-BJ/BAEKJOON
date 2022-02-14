#BOJ 1912
num = int(input())
seq = list(map(int, input().split()))

dp = [-1001]*100001

for i in range(num):
    dp[i] = max(dp[i-1]+seq[i], seq[i])
print(max(dp))