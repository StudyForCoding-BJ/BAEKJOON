#BOJ 10989 _ 2
#229B, 8732ms
#input 함수를 미리 지정해 놓았을 때 -> 시간 단축

import sys
input = sys.stdin.readline

num = int(input())

count = [0]*10001

for i in range(num):
    count[int(input())] += 1
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print (i)
