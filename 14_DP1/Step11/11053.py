#BOJ 11053
#212ms, 앞에서부터 처리하는 dp
num = int(input())
seq = list(map(int, input().split()))

dp = [0]*(num)

for i in range(num):
    if i == 0:
        dp[i] = 1
    else:
        j = 0
        tmp = 1
        while i > j:
            if seq[i] > seq[j]:
                tmp = dp[j]+1
            if dp[i] < tmp:
                dp[i] = tmp
            j += 1
print(max(dp))