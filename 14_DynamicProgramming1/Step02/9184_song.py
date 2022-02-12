import sys

#입력받기
arr = []
while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    arr.append([a, b, c])


#계산
def w(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    #값 존재하면 리턴
    if result[a][b][c]:
        return result[a][b][c]
    
    if a < b < c:
        result[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        result[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return result[a][b][c]

result = [[[0] * 21 for i in range(21)] for j in range(21)]

for i in range(len(arr)):
    result2 = w(arr[i][0], arr[i][1], arr[i][2])
    print(f'w({arr[i][0]}, {arr[i][1]}, {arr[i][2]}) = {result2}')