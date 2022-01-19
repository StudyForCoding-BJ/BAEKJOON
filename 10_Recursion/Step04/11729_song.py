N = int(input())
arrx = []
arry = []

def move(n:int, x:int, y:int) -> None :
    if n > 1:
        move(n-1, x, 6 - x - y)

    arrx.append(x)
    arry.append(y)
    

    if n > 1:
        move(n-1, 6 - x - y, y)





move(N, 1, 3) #원반개수, 시작기둥, 끝기둥

print(len(arrx))

for i in range(len(arrx)):
    print(arrx[i], arry[i])
