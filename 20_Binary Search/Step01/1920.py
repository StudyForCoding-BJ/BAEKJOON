#BOJ 1920
#recursion Binary Search
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
tc = list(map(int, input().split()))

def bin(arr: list, l: int, r: int, t: int):
    if l > r:
        return 0
    
    m = (l+r)//2
    
    if arr[m] == t:
        return 1
    elif arr[m] < t:
        return bin(arr, m+1, r, t)
    else:
        return bin(arr, l, m-1, t)

for i in tc:
    print(bin(a, 0, n-1, i))