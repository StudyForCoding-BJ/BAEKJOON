# 72ms
# 30864KB

oper = input().split('-')
result = 0

#맨 앞 연산 먼저 계산
for i in oper[0].split('+'):
    result += int(i)

# 그 뒤로는 + 계산해서 s에서 뺌
for i in oper[1:]:
    for j in i.split('+'):
        result -= int(j)
        
print(result)