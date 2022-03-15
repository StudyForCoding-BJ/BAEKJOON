#BOJ 10816 _ 3
#744ms
#2에서의 정렬, key를 set으로 바꾸는 과정 등이 사실상 불필요하다.
#딕셔너리로 받을 때 이미 key로 in 연산을 O(1)으로 수행할 수 있기 때문.
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
tc = list(map(int, input().split()))
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print('\n'.join(str(d[j]) if j in d else '0' for j in tc))