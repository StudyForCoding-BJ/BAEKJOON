N = int(input())

count = 0
i = 665
while 1:
    if(count == N):
        print(i-1)
        break
    else:
        if str(i).find("666") != -1:
            count += 1
        i += 1




