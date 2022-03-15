#BOJ 2740
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

m, k  = map(int, input().split())
b = [list(map(int, input().split())) for i in range(m)]

fin = []

for l in range(n):
    llst = []
    for j in range(k):
        res = 0
        for i in range(m):
            res += a[l][i]*b[i][j]
        llst.append(res)
    fin.append(llst)

for i in range(n):
    print(*fin[i])
    
# fin = [[0] * K for _ in range(N)] 로 최종행렬을 초기 선언하고 실행하면 
# 약 40ms 정도 시간이 더 걸림