#BOJ 12865
#2차원 배열 2개, 279000KB, 7516ms

import sys

num, max_weight = map(int, sys.stdin.readline().split())
have = []
for i in range(num):
    have.append(list(map(int, sys.stdin.readline().split())))

memo = [[0]*(max_weight+1) for i in range(num+1)]

for i in range(1, num+1):
    for j in range (1, max_weight+1):
        if j - have[i-1][0] >= 0:
            memo[i][j] = max(memo[i-1][j-have[i-1][0]] + have[i-1][1], memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]
print(memo[num][max_weight])