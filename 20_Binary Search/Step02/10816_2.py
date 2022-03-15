#BOJ 10816 _ 2
#dict와 set, in의 조합
import sys
input = sys.stdin.readline

n = int(input())
a = {}
for i in list(map(int, input().split())):
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
arr = set(sorted(a))
m = int(input())
tc = list(map(int, input().split()))

for i in tc:
    if i in arr:
        print(a[i])
    else:
        print(0)