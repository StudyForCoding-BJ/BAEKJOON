#BOJ 12865 _ better _ 1
#2차원 배열 1개, 1차원 배열 2개. 281052KB, 6524ms
#1차원 배열 2개는 2차원 배열 1개와 메모리 차이가 크게 나지 않는다.
#하지만 1차원 배열 2개가 2차원 배열을 연산하는 것보다 더 유리하다.

import sys

num, max_weight = map(int, sys.stdin.readline().split())
weight = [0]
value = [0]
for i in range(num):
    e1, e2 = map(int, sys.stdin.readline().split())
    weight.append(e1)
    value.append(e2)

memo = [[0]*(max_weight+1) for i in range(num+1)]

for i in range(1, num+1):
    for j in range (1, max_weight+1):
        if j - weight[i] >= 0:
            memo[i][j] = max(memo[i-1][j-weight[i]] + value[i], memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]
print(memo[num][max_weight])