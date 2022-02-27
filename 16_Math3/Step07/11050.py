#BOJ 11050 _ 1(lib)
#32976KB, 80ms (math만 import)
#32976KB, 76ms(comb만 import)
#import를 뭘 하느냐의 차이는 아닌 것 같고 서버 상의 시간 단축인듯
from math import comb
n, k = map(int, input().split())
print(comb(n, k))