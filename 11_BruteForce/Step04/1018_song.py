N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(input())

#8 X 8로 나누기
def divide(N: int, M: int, arr: list) -> list:
    m = 0
    n = 0
    count = []
    
    while n+7 < N:
        m = 0
        while m+7 < M:
            arr2 = []
            for j in range(n, n+8):
                temp = ''
                for i in range(m, m+8):
                    temp += arr[j][i]
                arr2.append(temp)
            #8x8 완성
            count.append(color(arr2))
            
            m = m + 1
        n = n + 1
    return count

#다시 칠해야 할 칸 수 구하기
def color(arr: list) -> int:
    count1 = 0
    count2 = 0
    #W로 시작할 경우
    for n in range(0, 7, 2): # n 짝수
        for m in range(0, 7, 2):
            if arr[n][m] != 'W':
                count1 += 1
            else:
                pass
        for m in range(1, 8, 2):
            if arr[n][m] != 'B':
                count1 += 1
            else:
                pass
    for n in range(1, 8, 2): # n 홀수
        for m in range(1, 8, 2):
            if arr[n][m] != 'W':
                count1 += 1
            else:
                pass
        for m in range(0, 7, 2):
            if arr[n][m] != 'B':
                count1 += 1
            else:
                pass
        
    #B로 시작할 경우
    for n in range(0, 7, 2): # n 짝수
        for m in range(0, 7, 2):
            if arr[n][m] != 'B':
                count2 += 1
            else:
                pass
        for m in range(1, 8, 2):
            if arr[n][m] != 'W':
                count2 += 1
            else:
                pass
    for n in range(1, 8, 2): # n 홀수
        for m in range(1, 8, 2):
            if arr[n][m] != 'B':
                count2 += 1
            else:
                pass
        for m in range(0, 7, 2):
            if arr[n][m] != 'W':
                count2 += 1
            else:
                pass
    return min(count1, count2)

count = divide(N, M, arr)
print(min(count))
