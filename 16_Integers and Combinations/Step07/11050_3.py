#BOJ 11050
#직접 for문으로 팩토리얼 구현 -> 30864KB, 72ms
n, k = map(int, input().split())
def fact(a: int):
    res = 1
    for i in range(1, a+1):
        res *= i
    return res
print(fact(n)//fact(k)//fact(n-k))