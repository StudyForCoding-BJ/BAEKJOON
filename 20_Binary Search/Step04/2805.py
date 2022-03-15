#BOJ 2805
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

def check(a: int):
    cnt = 0
    for i in t:
        tmp = i-a
        if tmp > 0:
            cnt += tmp
        else:
            continue
    return cnt

def bin(l: int, r: int, t: int):
    if l>r:
        return r
    mid = (l+r)//2
    tmp = check(mid)
    if tmp >= t:
        return bin(mid+1, r, t)
    else:
        return bin(l, mid-1, t)
print(bin(1, max(t), m))