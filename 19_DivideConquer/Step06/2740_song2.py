# BOJ 2740
# 244ms
# 30864KB

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)] # 최종행렬 N x K
for i in range(N):
    for j in range(K):
        for a in range(M):
            result[i][j] += matrix1[i][a] * matrix2[a][j]
    
for i in range(N):
    for j in range(K):
        print(result[i][j], end=' ')
    print()