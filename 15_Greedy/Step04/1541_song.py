# 136ms
# 33504KB

# 처음에 문자열로 된 수식 계산하려고 eval 썼지만 0으로 시작하는 숫자 처리 못함
# 앞에 0이 붙은 숫자 처리 ->  앞에 0x를 붙여주거나 int('0009') 

import re

# - 기준으로 수식 자르기
arr = input().split('-') 

# 문자열에서 숫자 추출 -> 나눠진 숫자들 합
numbers = []
for i in arr:
    temp = list(map(int, re.findall("\d+", i))) 
    numbers.append(sum(temp))

# - 연산
result = numbers[0]
for i in range(1, len(numbers)):
    result -= numbers[i]
    
print(result)

