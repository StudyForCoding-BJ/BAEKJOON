#BOJ 11444
#피보나치 분할정복법 https://cupjoo.tistory.com/20
n = int(input())

mtx = [[1, 1], [1, 0]]

mod = 1000000007

def dot(mtx1: list, mtx2: list):
    fin = []
    for l in range(2):
        llst = []
        for j in range(2):
            res = 0
            for i in range(2):
                res += mtx1[l][i]*mtx2[i][j]
            res = res%mod
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

print(dq(n)[0][1]%mod)