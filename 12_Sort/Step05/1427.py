#BOJ 1427
#62B, 72ms
#74B, 68ms로 다른 사람은 num.sort() 후에 list를 뒤집어서 end=''로 하나씩 출력함.
#크게 다를 건 없어 보여서 이대로 업로드

num = list(input())
num.sort(reverse=True)
print(''.join(num))