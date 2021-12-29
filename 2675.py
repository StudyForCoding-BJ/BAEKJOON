#BOJ 2675

totalTC = int(input())

for i in range(totalTC):
    info = input()
    infolist = info.split()
    repStr = infolist[1]
    
    res = ""
    
    #Repeat
    for i in repStr:
        res = res + i*int(infolist[0])
    print (res)