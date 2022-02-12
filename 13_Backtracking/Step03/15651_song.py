#964ms

N, M = map(int, input().split())

data = []
for i in range(1, N + 1):
    data.append(i)
    
output=[]

def NM(letter):
    if len(letter) >= M:
        print(' '.join(list(letter)))

    else:
        for k in data:
            NM(letter + str(k))
                    
for i in range(N):
    NM(str(data[i]))