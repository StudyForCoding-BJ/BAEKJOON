N = int(input())

def fibo(n:int) -> int:
    if(n > 1):
        return fibo(n-2) + fibo(n-1)
    elif(n == 1):
        return 1
    else:
        return 0

print(fibo(N))
        
