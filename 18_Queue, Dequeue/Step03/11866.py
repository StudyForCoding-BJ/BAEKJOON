#BOJ 11866
#128ms, 출력 방법은 string[1:-1]이나 아래의 방법이나 차이 없음.

from collections import deque
n, k = map(int, input().split())
dq = deque(range(1, n+1))
res = []
while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())
ans = ', '.join(map(str, res))
print(f'<{ans}>')