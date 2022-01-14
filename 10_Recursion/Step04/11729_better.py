#BOJ 11729_better
#908ms

def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, aux, end)
    print(start, end)
    
    hanoi(n-1, aux, end, start)

num = int(input())
print(2**num -1)
hanoi(num, 1, 3, 2)