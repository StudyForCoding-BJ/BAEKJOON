num = int(input())

def sum(n):
    sum = 0
    for i in range(1, n):
        sum += i
    return sum
#섹션찾기
stand = 0
cnt =1
while (num > stand):
    stand += cnt
    cnt +=1

cnt = cnt - 1

secnum = num - sum(cnt) #섹션 중 몇번쨰인지 찾기
a = cnt-secnum+1

if(cnt%2 == 0):
    print( secnum, '/', a, sep='')
else:
    print( a, '/', secnum, sep='')
    
