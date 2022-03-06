# BOJ 10830
# 76ms
# 30864KB

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        matrix[i][j] %= 1000

result = [[1] * N for _ in range(N)]

# 두 행렬 곱
def matrix_multi(m1, m2):
    
    temp_multi = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for a in range(N):
                temp_multi[i][j] += m1[i][a] * m2[a][j] 
            temp_multi[i][j] %= 1000
    return temp_multi

# 행렬 거듭제곱(분할정복)   
def power(n):
    
    global result, matrix 
    
    if n == 1:
        return matrix
    else:
        if n % 2 != 0:
            n = n // 2
            temp = power(n)
            result = matrix_multi(matrix_multi(temp , temp), power(1))
        else:
            n = n // 2
            temp = power(n)
            result = matrix_multi(temp , temp)
        return result

final_result = power(B)    
for i in range(N):
    print(*final_result[i])
    
'''
반례
2 1
1000 1000
1000 1000
했을 때 
0 0
0 0
이 나와야하는데 초기화한 result값인
1 1
1 1 이 나옴
'''