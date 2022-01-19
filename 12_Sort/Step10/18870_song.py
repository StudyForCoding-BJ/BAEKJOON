N = int(input())

data = list(map(int, input().split()))
    
cnt = sorted(list(set(data)))

dictionary = {cnt[i]:i for i in range(len(cnt))}
        
for i in data:
    print(dictionary[i], end = ' ')
