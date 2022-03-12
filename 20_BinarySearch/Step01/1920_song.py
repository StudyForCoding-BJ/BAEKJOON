# BOJ 1920
# 720ms
# 46308KB
# 재귀 안쓰고 wile문으로 푸는 게 약 100ms 정도 빠른듯함

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
findmem = list(map(int, input().split()))

arr.sort()

def binary_search(arr, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == num:
        return 1
    elif arr[mid] < num:
        return binary_search(arr, mid+1, end)
    else:
        return binary_search(arr, start, mid-1)
    
for i in range(M):
    num = findmem[i]
    print(binary_search(arr, 0, len(arr)-1))
    