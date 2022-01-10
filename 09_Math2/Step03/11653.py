#BOJ 11653

def sep(a: int):
    for i in range(2, a+1):
        while a%i==0:
            print(i)
            a = a//i
sep(int(input()))