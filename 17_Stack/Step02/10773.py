#BOJ 10773
#124ms가 나왔는데 116ms가 나온 다른 답안과 비교했을 때 완전 똑같아서 서버 차이인걸로
#remove와 pop 중 어떤 것을 쓸 것인지 고민
#파이썬 리스트 내장함수 시간복잡도 참고 링크 -> https://chancoding.tistory.com/43
import sys
num = int(input())
st = []
for i in range(num):
    a = int(sys.stdin.readline())
    if a == 0:
        st.pop()
    else:
        st.append(a)
print(sum(st))