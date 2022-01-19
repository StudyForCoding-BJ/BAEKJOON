import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    d = int(sys.stdin.readline().strip())
    data.append(d)

def counting_sort(data : list, m: int) -> list:
    freq = [0] * (m+1)

    #data 빈도수 파악
    for i in data:
        freq[i] += 1

    #freq 앞 요소만큼 더해주기
    for i in range(1,m+1):
        temp = 0
        for j in range(i):
            temp = freq[j]
        freq[i] += temp

    #input_arr의 요소값 output_arr에 채워넣기
    output = [-1] * len(data)
    
    for i in data:
        output[freq[i]-1] = i
        freq[i] -= 1
        
    return output
            
        
m = max(data)
result = counting_sort(data, m)

for i in result:
    print(i)







#https://elrion018.tistory.com/37
