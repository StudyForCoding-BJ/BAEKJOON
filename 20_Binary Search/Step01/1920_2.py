#BOJ 1920 _ 2
#in 함수와 set 조합. -> O(1)
#https://twpower.github.io/120-python-in-operator-time-complexity
#200ms
import sys
n = int(input())
a = set(map(int, input().split()))
m = int(input())
tc = list(map(int, input().split()))

for i in tc:
    print(int(i in a))