#768ms

first = input()
second = input()

first_len = len(first)
second_len = len(second)
arr = [[0 for col in range(second_len+1)] for row in range(first_len+1)]

for i in range(1, first_len+1):
    f = first[:i] # i번째까지 문자열 슬라이싱
    for j in range(1, second_len+1):
        s = second[:j] # j번째까지 문자열 슬라이싱
        if f[-1] == s[-1]: # 마지막 문자가 같으면
            arr[i][j] = arr[i-1][j-1] + 1 # CS로 간주
        else: # 마지막 문자가 다르면
            arr[i][j] = max(arr[i-1][j], arr[i][j-1]) #이전 값 중 max 값

print(arr[first_len][second_len])
 
        
        
# 문자열 슬라이스
# print(first[:2]) -> 2번 인덱스 전까지 끊음