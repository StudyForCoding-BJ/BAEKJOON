# BOJ 2740
# 260ms
# 30864KB

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)] # 최종행렬 N x K
for i in range(N): # N
    temp = []
    for j in range(M):
        temp.append(matrix1[i][j]) # matrix1의 행 / temp = [1, 2]
        
    for k in range(K):
        temp2 = []
        for m in range(M):
            temp2.append(matrix2[m][k]) # matrix2의 열 / temp2 = [-1, 0]
            
        temp3 = 0
        for just in range(M):
            temp3 += temp[just] * temp2[just] # 두 matrix의 행과 열 곱 / temp3 = 1 * -1 + 2 * 0
        result[i][k] = temp3
            
for i in range(N):
    print(*result[i])
        