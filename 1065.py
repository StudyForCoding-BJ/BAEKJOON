#BOJ 1065

#receive a number and check if it is 한수
def spNum(num: int):
    tmpStr = str(num)
    #store each number in string
    tmplist = list(tmpStr)
    
    #count gap
    gap = int(tmplist[0]) - int(tmplist[1])
    
    #check each gap
    for i in range (0, len(tmplist)-1):
        if gap == int(tmplist[i]) - int(tmplist[i+1]):
            continue
        else:
            return False

#Input number (string)
maxNumStr = input()
#Input to Integer
maxNum = int(maxNumStr)

#1~9
cntNum = 9

#if the input has one digit
if maxNum < 10:
    print (maxNum)
#input has digits more than one
else:
    for i in range (10, maxNum+1):
        if spNum(i) != False:
            cntNum += 1
    print (cntNum)