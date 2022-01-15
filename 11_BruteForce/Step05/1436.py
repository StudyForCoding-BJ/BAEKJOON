#BOJ 1436
#

numList = []
for i in range(4000000):
    if "666" in str(i):
        numList.append(i)
print(numList[int(input())-1])