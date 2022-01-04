N = int(input())

a = [0] * N #반복할 숫자
b = [0] * N #반복할 문자열

for i in range(N):
    a[i], b[i] = input().split()

for i in  range(N):
    result=''
    for arr in b[i]:
        result += arr * int(a[i])
    print(result)
