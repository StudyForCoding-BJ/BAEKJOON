# 68ms
# 30860KB
import sys
N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())
    arr = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
    
    # 옷 종류
    cloth_type = []
    for j in arr:
        if j[1] not in cloth_type:
            cloth_type.append(j[1])
    
    # 종류별 개수        
    type_num = [0] * len(cloth_type)
    for k in range(len(arr)):
        for m in range(len(cloth_type)):
            if arr[k][1] == cloth_type[m]:
                type_num[m] += 1
    
    # 경우의 수 계산
    result = 1
    for case in type_num:
        result *= (case + 1) # 선택 안할 경우 포함
                
    print(result-1)
    