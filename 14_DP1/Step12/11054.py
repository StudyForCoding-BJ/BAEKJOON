#BOJ 11054
#344ms, 30864KB
num = int(input())
seq = list(map(int, input().split()))

inc = [0]*(num)

#increase
for i in range(num):
    if i == 0:
        inc[i] = 1
    else:
        j = 0
        tmp = 1
        while i > j:
            if seq[i] > seq[j]:
                tmp = inc[j]+1
            if inc[i] < tmp:
                inc[i] = tmp
            j += 1
dec = [0]*(num)
for i in range(num-1, -1, -1):
    if i == num-1:
        dec[i] = 1
    else:
        j = num-1
        tmp = 1
        while i < j:
            if seq[i]>seq[j]:
                tmp = dec[j]+1
            if dec[i]<tmp:
                dec[i] = tmp
            j -= 1
res = 0
for i in range(num):
    if res < inc[i]+dec[i]-1:
        res = inc[i]+dec[i]-1
print(res)