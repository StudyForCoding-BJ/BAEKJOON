# BOJ 2805
# 2812ms
# 143064KB

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
while start <= end:
    total = 0
    mid = (start + end) // 2
            
    for i in arr:
        if i > mid: # 나무가 절단기보다 높을때만 나무가 남음
            total += i - mid
            if total >= M: # 이러면 for문 더 안돌아도 됨
                break
        
    if total < M: # 더 작게 자르기
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
