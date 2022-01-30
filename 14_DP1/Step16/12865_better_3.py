#BOJ 12865 _ better _ 2
#1차원 배열 3개. 33688KB, 5368ms
#2차원 배열을 1차원 배열 2개로 쪼갠다고 메모리 상에서 이득이 된다는 건 아님을 보여주는 예 2
#그러나 확실히 시간적 이득은 있음

#for문 안에 입력까지 같이 넣어서 앞에서부터 처리하는 방법이 4000ms정도 걸리는 것 같은데 그냥 그런 방법도 있다 정도로만 이해함.

import sys

num, max_weight = map(int, sys.stdin.readline().split())
weight = [0]
value = [0]
for i in range(num):
    e1, e2 = map(int, sys.stdin.readline().split())
    weight.append(e1)
    value.append(e2)

memo = [0]*(max_weight+1)

for i in range(1, num+1):
    for j in range(max_weight, 0, -1):
        if j - weight[i] >= 0 :
            memo[j] = max(memo[j-weight[i]] + value[i], memo[j])
print(memo[max_weight])