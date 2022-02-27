#68ms

num = int(input())
factors = list(map(int, input().split()))

factors.sort()
if num == 1:
    print(factors[0]*factors[0])
else:
    print(factors[0]*factors[-1])