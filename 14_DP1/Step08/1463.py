#BOJ 1463
#884ms, 78232KB
#한번에 연산을 처리하면 중복연산이 생김
num = int(input())
seq = list(range(num+1))

dp = [0]*(num+1)

for i in range(1, num+1):
    if i == 1:
        dp[i] = 0
    elif i == 2 or i == 3:
        dp[i] = 1
    else:
        dp[i] = min(dp[(i-(i%3))//3]+(i%3)+1, dp[(i-(i%2))//2]+(i%2)+1)
print(dp[num])

'''
이 풀이와 왜 그렇게 차이가 나는지 알아보기
38302856
39112KB, 500ms
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
'''