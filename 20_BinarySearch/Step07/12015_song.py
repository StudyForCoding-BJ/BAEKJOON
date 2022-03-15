# BOJ 12015
# 1052ms
# 146156KB

import sys, bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
mem = [0]

for i in arr:
    if i > mem[-1]:
        mem.append(i)
    else:
        # bisect_left: 정렬된 순서를 유지하면서 mem에 데이터 i를 삽입할 가장 왼쪽 인덱스 찾기
        # lo=1: mem의 1번째 인덱스부터 탐색
        # mem[-1]보단 작은데 그 안에 들어갈 수 있는 수는 i로 바꿔줌
        mem[bisect.bisect_left(mem, i, lo=1)] = i 

print(len(mem)-1)
         