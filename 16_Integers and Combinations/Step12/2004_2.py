#BOJ 2004 _ 2
#연산 수 줄이기 -> 76ms (a//5가 반복되는 걸 줄임)
n, m = map(int, input().split())
d = n-m
def fivecnt(a: int):
    cnt = 0
    while a > 0:
        a = a//5
        cnt += a
    return cnt
def twocnt(a: int):
    cnt = 0
    while a > 0:
        a = a//2
        cnt += a
    return cnt
print(min(fivecnt(n)-fivecnt(m)-fivecnt(d), twocnt(n)-twocnt(m)-twocnt(d)))