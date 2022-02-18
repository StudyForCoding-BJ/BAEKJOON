# 156ms
# 45748KB

N = int(input())
dis = list(map(int, input().split()))
L = list(map(int, input().split()))

L[N-1] = 10001
count = 0
for i in range(N-1):
    if L[i] < L[i+1]: # 현재 주유소가 더 싸면
        L[i+1] = L[i] # 다음 주유소 가격을 현재 주유소로 바꾸기
    count += L[i] * dis[i]
        
print(count)