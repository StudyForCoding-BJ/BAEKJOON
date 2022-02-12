#416ms

N = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0) # 배열 처음에 0 삽입
arr.append(0) # 배열 끝에 0 삽입

temp_first = [0] * (N+2)
temp_last = [0] * (N+2)

for i in range(1, N+1):
    for j in range(i):
        #왼쪽에서부터 LIS 찾기
        if arr[j] < arr[i]:
            temp_first[i] = max(temp_first[i], temp_first[j]+1)
        #오른쪽에서부터 LIS 찾기
        a = N-i+1
        b = N-j+1
        if arr[b] < arr[a]:
            temp_last[a] = max(temp_last[a], temp_last[b]+1)

#두 배열 합
add_list = [temp_first[i] + temp_last[i] for i in range(len(temp_first))]
print(max(add_list)-1)