#BOJ 4948

def era(start, end: int):
    era = [1]*(end+1)
    era[1] = 0

    for i in range(2, int(end**0.5)+1):
        if era[i] == 1:
            for j in range(i*2, end+1, i):
                era[j] = 0

    cnt = 0
    for i in range(start, end+1):
        if era[i] == 1:
            cnt+=1
    return cnt

while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(era(num+1,2*num))