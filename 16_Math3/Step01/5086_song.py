#68ms
#30860KB
import sys

arr = []
arr.append([10001, 10001])
while arr[-1][0] != 0:
    arr.append(list(map(int, sys.stdin.readline().split())))
    
def relation(case):
    if case[0] < case[1]:
        if case[1] % case[0] == 0:
            print("factor")
            return
    else:
        if case[0] % case[1] == 0:
            print("multiple")
            return
    print("neither")
    return

for i in range(1, len(arr)-1):
    relation(arr[i])