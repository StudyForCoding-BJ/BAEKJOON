#BOJ 10872

def fact(a:int):
    if a == 0:
        return 1
    return fact(a-1) * a

print(fact(int(input())))