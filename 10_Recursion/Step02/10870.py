#BOJ 10870

def fib(a:int):
    if a==0:
        return 0
    elif a==1:
        return 1
    return fib(a-1) + fib(a-2)

print(fib(int(input())))