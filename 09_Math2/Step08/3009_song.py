x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

#중복제거
temp = []
for j in x:
    if j not in temp:
        temp.append(j)
        
temp2 = []
for k in y:
    if k not in temp2:
        temp2.append(k)

#카운트
for m in range(len(temp)):
    if(x.count(temp[m]) == 1):
        resultx = temp[m]

for n in range(len(temp2)):
    if(y.count(temp2[n]) == 1):
        resulty = temp2[n]

print(resultx, resulty)
