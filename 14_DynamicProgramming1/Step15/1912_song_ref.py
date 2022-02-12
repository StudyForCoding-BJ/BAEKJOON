#116ms

'''
보완한 점
- 입력수열을 DP배열에 복사 -> max함수 안쓰게 함
- import sys로 입력값 받게 함
'''

import sys
N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))

arr = seq[:] #입력수열 복사

# 자기자신을 포함하는 연속합의 최대값
for i in range(1, N):
    if seq[i] < seq[i] + arr[i-1]: # 자기자신 < 자기자신 + 이전 연속합의 최대값 이면
        arr[i] = seq[i] + arr[i-1] # 배열에 큰 값 저장
    
print(max(arr))