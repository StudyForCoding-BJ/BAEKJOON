#BOJ 11650 _ 2
#199B, 400ms
#input 함수를 따로 빼지 않았을 때 걸리는 시간 -> 오히려 시간이 단축됐다. BOJ 채점 서버 상의 문제거나
#어쨌든 간에 함수를 따로 빼고 말고는 큰 영향은 없는 것 같음.

import sys

num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x: (x[0], x[1]))
for i in data:
    print(*i, sep=' ')