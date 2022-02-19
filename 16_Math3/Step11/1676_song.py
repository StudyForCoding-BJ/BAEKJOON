# 72ms
# 31032KB

N = int(input())

def factorial(n: int) :
    if n == 0:
        return 1
    else:
        num = n * factorial(n-1)
    return num

# 팩토리얼 결과 문자열로 바꿔서 처리
result = str(factorial(N))
count = 0
for i in result[::-1]:
    if i != '0':
        break
    count += 1
    
print(count)
