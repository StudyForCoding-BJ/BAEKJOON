#BOJ 10989 _ 3
#198B, 8772ms
#input 함수를 미리 지정해 놓고, count[i] == 0인지 확인하는 조건문  -> 시간 단축에 영향 X

import sys
input = sys.stdin.readline

num = int(input())

count = [0]*10001

for i in range(num):
    count[int(input())] += 1
for i in range(10001):
    for j in range(count[i]):
        print (i)
