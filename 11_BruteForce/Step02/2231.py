#BOJ 2231
#72ms
'''
68ms, shorter code: 자리수 때문에 a의 구간을 나눠줬는데
그럴 필요 없이 한계(999,999)까지 생각해서 range(max(0, a-54), a)로 할 수 있다.
또한 str으로 바꿨다 int로 바꿨다 하는 부분을 한 줄로 i+sum(int(j) for j in str(i))로 할 수 있다.
'''

def const(a: int):
    if a>=1 and a<19:
        for i in range(1, a):
            if i + i//10 + i%10 == a:
                return i
            else:
                continue
    else:
        length = len(str(a))
        for i in range(a-length*9, a):
            sum = i
            for j in str(i):
                sum += int(j)
            if sum == a:
                return i
            else:
                continue
    return 0
        
print(const(int(input())))