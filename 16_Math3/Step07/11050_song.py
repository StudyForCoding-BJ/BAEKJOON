# 76ms
# 30864KB

N, K = map(int, input().split())

nu = 1 # 분자
de = 1 # 분모

for i in range(1, K+1):
    nu *= N - i + 1
    de *= i
    
print(nu//de)