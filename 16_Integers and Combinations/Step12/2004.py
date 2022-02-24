#BOJ 2004
#88ms
n, m = map(int, input().split())
d = n-m
def fivecnt(a: int):
    cnt = 0
    while a//5 > 0:
        cnt += a//5
        a = a//5
    return cnt
def twocnt(a: int):
    cnt = 0
    while a//2 > 0:
        cnt += a//2
        a = a//2
    return cnt
print(min(fivecnt(n)-fivecnt(m)-fivecnt(d), twocnt(n)-twocnt(m)-twocnt(d)))