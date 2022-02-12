# 200ms 
# max로 찾는 시간이 더 걸리는구나..

N = int(input())

arr = list(map(int, input().split()))
# arr.insert(배열 인덱스, 데이터)
arr.insert(0, 0) 

# DP저장 배열
temp = [0] *(N+1)

for i in range(1, N+1):
    for j in range(i):
        if arr[j] < arr[i]: 
            temp[i] = max(temp[i], temp[j]+1) # temp 최대값 구하는 과정
    
print(max(temp))