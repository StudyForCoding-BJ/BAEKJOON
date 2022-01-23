#BOJ 1904
#Bottom-up인건 알고 있었는데 숫자가 크면 연산에 시간이 걸려서 시간 초과가 난다는 걸 몰랐다
#264ms, 99B

num = int(input())

a= 1
b = 1

for i in range(2, num+1):
    a, b = b%15746, (a+b)%15746

print(b)