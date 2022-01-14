#BOJ 11720

totalNum = int(input())
numstr = input()
eachNum = list(numstr)
"""
if totalNum != len(eachNum):
    print("input error")
"""
res = 0
for i in range(0, len(eachNum)):
    res = res + int(eachNum[i])
print (res)