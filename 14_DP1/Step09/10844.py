#BOJ 10844
#72ms

length = int(input())

memo = [[0]*11 for i in range(length+1)]

for i in range(1, 10):
    memo[1][i] = 1

for i in range(2, length+1):
    memo[i][0] = memo[i-1][1]
    for j in range(1, 10):
        memo[i][j] = (memo[i-1][j-1] + memo[i-1][j+1])%1000000000
print(sum(memo[length])%1000000000)