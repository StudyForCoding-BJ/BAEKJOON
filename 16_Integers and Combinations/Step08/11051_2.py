#BOJ 11051 _ 2 (lib)
#n과 k는 애초에 1000 이하의 수이므로 변화가 없다
#11051_1과 동일
from math import comb
n, k = map(int, input().split())
print(comb(n%10007, k%10007)%10007)