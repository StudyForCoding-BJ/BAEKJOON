# BOJ 1655
# 260ms
# 36872KB

import sys, heapq
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

def mid_heap():
    n = int(input())
        
    if i % 2 != 0: # 홀수일 경우 left에 넣기 (최대)
        heapq.heappush(left_heap, -n)
    else: # 짝수일 경우 right에 넣기 (최소)
        heapq.heappush(right_heap, n)
        
    # left보다 작은 값을 넣으면 right에 중간값보다 작은 원소가 들어감
    # -> left, right 첫원소 바꿔줌
    if right_heap and -left_heap[0] > right_heap[0]:  
        temp_left = heapq.heappop(left_heap)
        temp_right = heapq.heappop(right_heap)
        heapq.heappush(right_heap, -temp_left)
        heapq.heappush(left_heap, -temp_right)

    print(-left_heap[0])

for i in range(1, N + 1):
    mid_heap()