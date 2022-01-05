#BOJ 5622

tstWord = input()
num = len(tstWord)
totalAlph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0
for i in tstWord:
    if 0 <= totalAlph.find(i) < 3 :
        res = res + 2
    elif 3 <= totalAlph.find(i) < 6:
        res = res + 3
    elif 6 <= totalAlph.find(i) < 9:
        res = res + 4
    elif 9 <= totalAlph.find(i) < 12:
        res = res + 5
    elif 12 <= totalAlph.find(i) < 15:
        res = res + 6
    elif 15 <= totalAlph.find(i) < 19:
        res = res + 7
    elif 19 <= totalAlph.find(i) < 22:
        res = res + 8
    else:
        res = res + 9
print (res+num)