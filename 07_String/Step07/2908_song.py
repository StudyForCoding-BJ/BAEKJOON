num = input().split()
result = list()

for i in range(2):
    temp = list()
    for a in range(2, -1, -1):
        temp.append(num[i][a])
    result.append("".join(temp))
        

if(int(result[0]) > int(result[1])):
    print(result[0])
else:
    print(result[1])
