N, M = map(int, input().split())
black = list(map(int, input().split()))

def Jack(black, M):
    i = 0
    j = 1
    k = 2
    result = 0
    while i < len(black) - 2:
        while j < len(black) - 1:
            while k < len(black):
               temp = black[i] + black[j] + black[k]
               k = k + 1
               if result <= temp <= M:
                   result = temp
            j = j + 1
            k = j + 1
        i = i + 1
        j = i + 1
        k = j + 1
        
    return result
        

print(Jack(black, M))
