#BOJ 1011

def leap(d: int):
    n = 2
    if d == 1:
        return 1
    elif d == 2:
        return 2
    else:
        while n >= 2:
            start = (n-1)*n
            end = n*(n+1)
            if d>start and d<=start+(end-start)/2:
                return n*2-1
            elif d>start+(end-start)/2 and d<=end:
                return n*2
            else:
                n+=1

for i in range(int(input())):
    start, end  = map(int, input().split())
    print (leap(end-start))