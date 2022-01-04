#BOJ 1712

numlist = list(map(int, input().split()))

a = numlist[0]
b = numlist[1]
c = numlist[2]


def num():
    if b >= c:
        return -1

    else:
        i = a//(c-b)
        return i+1

print (num())