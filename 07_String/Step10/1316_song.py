N = int(input())
S = list()

for i in range(N):
    S.append(input())

def group(arr1, arr2):
    for a in arr2:
        temp = []
        cnt = 0
        for j in range(len(arr1)):
            if(arr1[j] == a):
                temp.append(j)
                
        if(len(temp) == 1):
            pass
        
        for k in range(len(temp)-1):
            if(temp[k+1]-temp[k] != 1):
                cnt += 1
                return False
            else:
                cnt = 0
    
    if(cnt == 0):
        return True
    

count = 0
for i in range(N):
    word1 = S[i] #happy
    word2 = list(set(S[i])) #hapy
    result = group(word1, word2)
    
    if(result):
        count += 1
    else:
        pass

print(count)
