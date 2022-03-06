# BOJ 11444
# 72ms
# 30864KB

N = int(input())
P = 1000000007

if N == 0:
    print(0)
    exit(0)
    
matrixA = [[1, 1], [1, 0]]

result = [[1] * 2 for _ in range(2)]
# 두 행렬 곱
def matrix_multi(m1, m2):
    
    temp_multi = [[0] * 2 for _ in range(2)]
    
    for i in range(2):
        for j in range(2):
            for a in range(2):
                temp_multi[i][j] += m1[i][a] * m2[a][j] 
            temp_multi[i][j] %= P
            
    return temp_multi

# 행렬 거듭제곱(분할정복)   
def power(n):
    
    if n == 1:
        return matrixA
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

u0 = [[0], [1]]
A = power(N)

final = [[0] * 1 for _ in range(2)] # 최종행렬 2 x 1
for i in range(2):
    for j in range(1):
        for a in range(2):
            final[i][j] += A[i][a] * u0[a][j] % P

print(final[0][0])
