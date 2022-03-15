#BOJ 10816
import sys
input = sys.stdin.readline

n = int(input())
a = {}
for i in list(map(int, input().split())):
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
arr = sorted(a)
m = int(input())
tc = list(map(int, input().split()))

def bin(arr: dict, l: int, r: int, t: int):
    
    if l > r:
        return 0
    
    m = (l+r)//2
    
    if arr[m] == t:
        return a[arr[m]]
    elif arr[m] < t:
        return bin(arr, m+1, r, t)
    else:
        return bin(arr, l, m-1, t)

for i in tc:
    print(bin(arr, 0, len(arr)-1, i))