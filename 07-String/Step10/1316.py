#BOJ 1316

#check GroupWord function
def grpWord (a: str):
    
    #select unique char
    tmp = list("".join(dict.fromkeys(a)))
    
    if len(tmp) == 1:
        return 0
    
    for i in range(len(tmp)):
        pos = a.find(tmp[i])
        #print(a)
        #print(a.find(tmp[i]))
        a = a[1:]
        while a.find(tmp[i]) == pos:
            a = a[1:]
        if a.find(tmp[i]) == -1:
            continue
        else:
            return -1
    
    return 0
    

wordNum = int(input())
tstlist = []
for i in range(wordNum):
    tstWord = input()
    tstlist.append(grpWord(tstWord))
#print(tstlist)
print(tstlist.count(0))