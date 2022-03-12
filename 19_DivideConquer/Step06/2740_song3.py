

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]

result = []
# result = [[0] * K for _ in range(N)] # 최종행렬 N x K
for i in range(N):
    list = []
    for j in range(K):
        res = 0
        for a in range(M):
            res += matrix1[i][a] * matrix2[a][j]
        list.append(res)
    result.append(list)
        
for i in range(N):
    print(*result[i])

