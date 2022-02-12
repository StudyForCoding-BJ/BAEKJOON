#68ms

import sys
N = int(input())

data = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
data.sort(key=lambda x:x[0])

arr = [0] * N # 해당위치에서 겹치지 않고 올 수 있는 최대 전깃줄 개수 배열
for i in range(N):
    lis = 0
    for j in range(i):
        if data[i][1] > data[j][1]: #이 경우에 i번째 전깃줄과 겹치지 않게 올 수 있음
            if lis < arr[j]:
                lis = arr[j] 
    arr[i] = lis + 1
    
print(N-max(arr))
    