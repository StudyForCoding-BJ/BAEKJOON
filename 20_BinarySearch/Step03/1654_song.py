# BOJ 1654
# 96ms
# 30864KB

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

m = max(arr) # 가장 긴 랜선 길이 기준으로 이분탐색

result = 0
def cut(arr, start, end):
    global result 
    while start <= end:
        mid = (start + end) // 2
        if mid == 0: # 0으로 나눈거 막기위함
            mid = 1
            
        total = 0 # mid 길이로 랜선 잘랐을 때 나오는 랜선 개수
        for k in arr:
            total += k // mid 
        
        if total < N: # 더 작게 잘라야됨
            end = mid - 1
        else:
            result = mid
            start = mid + 1

cut(arr, 0, m)    
print(result)