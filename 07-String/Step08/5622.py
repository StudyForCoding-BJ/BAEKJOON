#BOJ 1522_BETTER sol

#Use list indexing
alphList = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
res = 0
tstWord = input()
for i in range(len(tstWord)):
    for j in alphList:
        if tstWord[i] in j:
            res += alphList.index(j) + 3    #each index + 2 = dial num, +1 for time
print (res)
