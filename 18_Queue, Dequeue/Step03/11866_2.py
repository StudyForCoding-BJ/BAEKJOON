#BOJ 11866 _ 2
#68ms, dq 대신 list 쓰는 방법. i+k-1라는 규칙이 있어서 리스트를 쓰는 게 오히려 빠른 것으로 보임
#사실 pop하는 위치까지 찾아가는거나 11866_1에서 그 수만큼 popleft() 하는거나 똑같지만
#1에서는 popleft하고 다시 뒤에 더하기도 해야하므로 약 2배의 시간이 걸릴 것으로 보임.
#dq에서도 remove로 할 수는 있으나 그러면 시간복잡도가 리스트랑 똑같아져서 dq를 쓸 이유가 없어짐
n, k = map(int, input().split())
dq = list(range(1, n+1))
res = []
idx = 0
while dq:
    idx = (idx+k-1)%len(dq)
    res.append(dq.pop(idx))
ans = ', '.join(map(str, res))
print(f'<{ans}>')