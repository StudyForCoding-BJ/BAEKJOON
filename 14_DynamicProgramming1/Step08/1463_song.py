N = int(input())

arr = [0] * (N+1)

for i in range(2, N+1):
    #2, 3 모두로 나누어떨어짐
    if i%2 == 0 and i%3 == 0:
        arr[i] = min(arr[i//3],arr[i//2], arr[i-1])+1
    #2로도, 3으로도 나누어떨어지지 않음
    elif i%2 != 0 and i%3 != 0:
        arr[i] = arr[i-1]+1
    #2로만 나누어 떨어짐
    elif i%2 == 0 and i%3 != 0:
        arr[i] = min(arr[i//2], arr[i-1])+1
    #3으로만 나누어 떨어짐
    else:
        arr[i] = min(arr[i//3], arr[i-1])+1
print(arr[N])
