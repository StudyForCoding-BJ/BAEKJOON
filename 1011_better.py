#BOJ 1011

def leap(d: int):
    n = 2
    if d == 1:
        return 1
    elif d == 2:
        return 2
    else:
        while True:
            if d <= n*(n+1):
                break
            n+=1
        if d<=n*n:
            return n*2-1
        else:
            return n*2

for i in range(int(input())):
    start, end  = map(int, input().split())
    print (leap(end-start))