#BOJ 1037
n = int(input())
a = list(map(int, input().split()))
a.sort()
if n%2 != 0:
    print(a[int(n//2)]**2)
else:
    print(a[(n//2)-1]*a[n//2])