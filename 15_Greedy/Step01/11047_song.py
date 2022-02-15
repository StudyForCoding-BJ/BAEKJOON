#72ms
#30864KB

import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

count = 0  
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if arr[i] <= K:
        unit = K // arr[i] #사용할 동전의 개수
        K -= arr[i] * unit 
        count += unit
        
print(count)
            
            