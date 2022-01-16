N = int(input())

def star(N: int, lit: list) -> list:
    arr = []
    if(N == 3):
        return lit
    else:
        for i in lit:
            arr.append(i * 3)
        for i in lit:
            arr.append(i + len(lit)*' ' + i)
        for i in lit:
            arr.append(i * 3)
            
    return star(N//3, arr)
            
    


init = ['***', '* *', '***']
result = star(N, init)
for i in result:
    print(i)

    
