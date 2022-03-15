# BOJ 1300
# 916ms
# 30864KB
# 재귀가 시간이 오래걸림

import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

def kth_num(start, end):
    
    global result
    
    if start > end:
        return
    mid = (start+end) // 2
    
    # mid보다 작은 수의 개수
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    if cnt >= k: # k번째 수 이상이면 더 작은 수의 개수 찾기
        result = mid
        return kth_num(start, mid - 1)
    else:
        return kth_num(mid + 1, end)
    
kth_num(1, N*N)
print(result)