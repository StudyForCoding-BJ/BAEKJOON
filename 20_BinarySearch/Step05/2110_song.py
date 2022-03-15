# BOJ 2110
# 652ms
# 38588KB

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

start = 1 # min gap
end = arr[-1] - arr[0] # max gap
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = arr[0] # 공유기 위치
    count = 1
    
    # 공유기 설치
    for i in range(N):
        if mid <= arr[i] - temp:
            temp = arr[i]
            count += 1
    # C개 이상의 공유기를 설치할 수 있는 경우
    if count >= C:
        start = mid + 1 # 거리를 증가시킴
        result = mid
        
    else:
        end = mid - 1 # 거리를 감소시킴
        
print(result)