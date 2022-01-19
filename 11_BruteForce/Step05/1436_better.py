#BOJ 1436 _ better
#Abt 167B, Abt 724ms

num = int(input())
start = 666

cnt = 0
while True:
    if "666" in str(start):
        cnt += 1
        if cnt == num:
            break
    start += 1
print(start)


#if를 if 안에 넣어서 666이 들어갈 때만 cnt==num인지 확인하기 때문에 시간단축
