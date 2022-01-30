#BOJ 12865 _ better _ 2
#2차원 배열 1개, 1차원 배열 1개. 33688KB, 6436ms
#메모리 차원에서 유의미한 방법. DP에 사용된 2차원 배열의 크기가 커서 그런 것으로 보임.
#하지만 2차원 DP를 1차원 DP로 바꾼 것에 유의미한 연산 감소는 보이지 않음.

import sys

num, max_weight = map(int, sys.stdin.readline().split())
have = []
for i in range(num):
    have.append(list(map(int, sys.stdin.readline().split())))

memo = [0]*(max_weight+1)

for i in range(1, num+1):
    for j in range(max_weight, 0, -1):
        if j - have[i-1][0] >= 0 :
            memo[j] = max(memo[j-have[i-1][0]] + have[i-1][1], memo[j])
print(memo[max_weight])