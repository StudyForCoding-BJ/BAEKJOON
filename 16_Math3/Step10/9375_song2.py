# 68ms
# 30860KB
# 시간은 다르지 않지만 중복제거나 count 이용 -> 코드 간결

import sys
N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())
    arr = [sys.stdin.readline().split()[1] for _ in range(n)]
  
    # 옷 종류 (중복제거)
    cloth_type = list(set(arr))
    
    # 종류별 개수    
    type_num = [] 
    for i in cloth_type:
        type_num.append(arr.count(i))
    
    # 경우의 수 계산
    result = 1
    for case in type_num:
        result *= (case + 1) # 선택 안할 경우 포함
                
    print(result-1) # 알몸인 경우 뺌
    