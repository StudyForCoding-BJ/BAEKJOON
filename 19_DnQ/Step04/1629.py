#BOJ 1629
#1st trial: tmp를 설정해주지 않아 너무 많은 중복 연산으로 시간 초과
#2nd trial: base case를 일부러 n=1일 때가 아닌 n=2일 때로 (a*a)%c로 하면 재귀를 얕게 들어갈 줄 알았는데 RecursionError가 났다
#3rd trial: sys.setrecursionlimit을 쓰려고 하다가 혹시 몰라서 n=1일 때로 잡았더니 통과했다
#왜지?
#-> n=3일 때를 생각해보자. n//3은 1이다. 2를 거치지 않고 바로 1이 되기 때문에 1을 처리해 주는 로직이 없어 무한 루프가 걸렸을 것
a, b, c = map(int, input().split())

def mult(n: int):
    if n == 1:
        return a%c
    tmp = mult(n//2)
    if n%2 == 0:
        res = (tmp*tmp)%c
    else:
        res = (((tmp*tmp)%c)*a)%c
    return res
print(mult(b))