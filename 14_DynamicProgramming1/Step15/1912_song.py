#132ms

N = int(input())

seq = list(map(int, input().split()))

arr = [0] * N # DP배열
arr[0] = seq[0] # 수열 첫 번째 요소는 자기자신이 최대값

# 자기자신을 포함하는 연속합의 최대값
for i in range(1, N):
    arr[i] = max(seq[i], seq[i] + arr[i-1]) #max(자기자신, 자기자신 + 이전 연속합의 최대값)
    
print(max(arr))