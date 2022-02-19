#시간초과

import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

arr_min = min(arr)
idx = arr.index(arr_min)

result = []
for i in range(arr_min - 1):
    # arr에서 min_arr로 모두 나누어 떨어지는지 확인
    count = 0
    for j in arr:
        if j % arr[idx] != 0:
            count += 1
            break
    if count == 0:
        result.append(arr[idx])
    for k in range(N):
        arr[k] -= 1

print(*result[::-1])