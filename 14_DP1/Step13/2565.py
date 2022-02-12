#BOJ 2565
#30860KB, 72ms
import sys
num = int(input())
pair = []
for i in range(num):
    n1, n2 = map(int, sys.stdin.readline().split())
    pair.append([n1, n2])
pair.sort(key=lambda x: x[0])

dp = [0]*(num)

for i in range(num):
    if i == 0:
        dp[i] = 1
    else:
        j = 0
        tmp = 1
        while i > j:
            if pair[i][1] > pair[j][1]:
                tmp = dp[j]+1
            if dp[i] < tmp:
                dp[i] = tmp
            j += 1
print(num-max(dp))