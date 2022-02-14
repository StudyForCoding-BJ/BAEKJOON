#BOJ 11053 _ 2
#196ms, 뒤에서부터 처리
num = int(input())
seq = list(map(int, input().split()))

dp = [1]*(num)
for i in range(num):
    for j in range(i-1, -1, -1):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))