# 156ms

N = int(input())

arr = list(map(int, input().split()))
# arr.insert(배열 인덱스, 데이터)
arr.insert(0, 0) 

# DP저장 배열
temp = [0] *(N+1)

for i in range(1, N+1):
    lis = 0  
    for j in range(i):
        #arr[i]보다 작은 값들 찾기
        if arr[j] < arr[i]: 
            # arr[i]보다 작은 값들 중 temp에서 최대 LIS값 구하기
            if lis < temp[j]:
                lis = temp[j]
    temp[i] = lis + 1
    
print(max(temp))