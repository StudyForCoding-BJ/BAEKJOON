S = list(map(int, input()))

S.sort()

for i in S[::-1]:
    print(i, end = '')

