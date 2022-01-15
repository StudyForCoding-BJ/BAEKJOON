#BOJ 10989
#214B, 9136ms
'''
이론상, int 자료형 데이터 갯수에 따른 메모리 사용량 -> 문제에서 주어진 10,000짜리 list는 8mb를 넘지 않는다.
'''
#https://velog.io/@yesterdaykite/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%ED%81%AC%EA%B8%B0
'''
문제에서 주어진 대로 특정 범위 내에서는 counting sort를 쓰는 게 빠를 수 있다.
10,000이 그렇게 크지 않은 범위라고 간주하고 전부 counting sort 적용. O(n+k) n=10^7, k=10^4
https://en.wikipedia.org/wiki/Counting_sort#Complexity_analysis
'''
'''
한 줄씩 입력받아서 리스트로도 문자열로도 받을 수 없다. 수가 10^7개니까 메모리를 지나치게 잡아먹는다.
따라서 입력 받을 때마다 수를 세준다.
'''

import sys

num = int(input())

count = [0]*10001

for i in range(num):
    count[int(sys.stdin.readline())] += 1
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print (i)
