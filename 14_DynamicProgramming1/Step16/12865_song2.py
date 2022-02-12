#7464ms <- DP Bottom-up 방식

import sys

N, K = map(int, sys.stdin.readline().split())

W = []
V = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    W.append(w)
    V.append(v)
    
knap = [[0] * (K+1) for i in range(N+1)] #DP 테이블

for n in range(1, N + 1):
    for k in range(1, K + 1):
        if k - W[n-1] >= 0:
            knap[n][k] = max(knap[n-1][k], knap[n-1][k-W[n-1]]+V[n-1])
        else:
            knap[n][k] = knap[n-1][k]
            
print(knap[N][K])
            
            
    