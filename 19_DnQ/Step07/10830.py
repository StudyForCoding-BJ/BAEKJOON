#BOJ 10830
import sys
n, b = map(int, input().split())
mtx = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        mtx[i][j] = mtx[i][j]%1000

def dot(mtx1: list, mtx2: list):
    fin = []
    for l in range(n):
        llst = []
        for j in range(n):
            res = 0
            for i in range(n):
                res += mtx1[l][i]*mtx2[i][j]
            res = res%1000
            llst.append(res)
        fin.append(llst)
    return fin

def dq(layer: int):
    if layer == 1:
        return mtx
    paramtx = dq(layer//2)
    if layer%2 == 0:
        return dot(paramtx, paramtx)
    else:
        return dot(dot(paramtx, paramtx), mtx)

for i in range(n):
    print(*dq(b)[i])