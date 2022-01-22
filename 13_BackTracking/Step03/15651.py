#BOJ 15651
#1548ms, 227B

end, num = map(int, input().split())

res = []

def dfs():
    if len(res) == num:
        print(' '.join(map(str,res)))
        return
    for i in range(1, end+1):
        res.append(i)
        dfs()
        del res[-1]
dfs()