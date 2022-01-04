s = input()
s2 = s.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = [0] * 26

for a in s2:
    for i in range(0, 26):
        if(a == alphabet[i]):
            L[i] += 1
            break

#배열에서 최댓값 찾기
count = 0
for l in L:
    if( l > count ):
        count = l

#최대값 중복 확인
result = 0
for b in L:
    if( b == count):
        result += 1

#출력
if( result >= 2 ):
    print('?')
else:
    ind = L.index(count)
    print(alphabet[ind].upper())
