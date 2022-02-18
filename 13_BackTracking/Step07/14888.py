#BOJ 14888
#112ms
size = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))
maxi = -1000000001
mini = 1000000001
def sol(res: int, idx: int):
    global maxi, mini
    if idx == size:
        if res > maxi:
            maxi = res
        if res < mini:
            mini = res
        return
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            if i == 0:
                sol(res+numbers[idx], idx+1)
            elif i == 1:
                sol(res-numbers[idx], idx+1)
            elif i == 2:
                sol(res*numbers[idx], idx+1)
            else:
                sol(int(res/numbers[idx]), idx+1)
            cal[i] += 1
    return

sol(numbers[0], 1)
print(maxi, mini, sep='\n')