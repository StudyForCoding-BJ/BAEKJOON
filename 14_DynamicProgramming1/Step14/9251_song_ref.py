#708ms
'''
문자열 각각 슬라이스 할 필요 없고 슬라이스 된 문자열의 마지막만 보면 되므로 
first[i] == second[j]로 비교만 하면 됨...
'''

n = list(input())
m = list(input())

n_len = len(n)
m_len = len(m)

dp = [[0] * (n_len + 1) for i in range(m_len + 1)]
for i in range(m_len):
    for j in range(n_len):
        if m[i] == n[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[m_len][n_len])