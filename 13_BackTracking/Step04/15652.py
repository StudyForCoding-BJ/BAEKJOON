#BOJ 15652
#92ms, 282B

end, num = map(int, input().split())

res = []

def dfs():
    if len(res) == num:
        print(' '.join(map(str,res)))
        return
    for i in range(1, end+1):
        if len(res) == 0 or i >= max(res):
            res.append(i)
            dfs()
            del res[-1]
dfs()