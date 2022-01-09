data = []

N = int(input())

for i in range(N):
    data.append(int(input()))    

#소수 판별 함수
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

#소수 리스트 저장(시간초과 해결)
arr=[]
for i in range(2, 10000):
    if(is_prime(i)):
        arr.append(i)

for a in data:    
    tmp = a//2
    for m in range(len(arr)):
        if(tmp == arr[m]):
            print(arr[m], arr[m])
            break
        
        elif(arr[m] > tmp):
            if(is_prime(a - arr[m])):
                print(a - arr[m], arr[m])
                break
            else:
                pass
                
            


