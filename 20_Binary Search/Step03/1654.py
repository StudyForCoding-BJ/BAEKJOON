#BOJ 1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = list(int(input()) for i in range(k))

def check(a: int):
    cnt = 0
    for i in range(k):
        cnt += lan[i]//a
    return cnt

def bin(l: int, r: int, t: int):
    if l > r:
        return r
    m = (l+r)//2
    tmp = check(m)
    if tmp >= t:
        return bin(m+1, r, t)
    else:
        return bin(l, m-1, t)

print(bin(1, max(lan), n))