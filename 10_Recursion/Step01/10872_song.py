N = int(input())

def factorial(n:int) -> int:
    if(n > 0):
        return n * factorial(n-1)
    else:
        return 1

print(factorial(N))