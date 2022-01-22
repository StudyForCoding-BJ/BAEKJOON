#BOJ 15651_lib
#중복 순열(product) 이용. -> O(k x Product of all n[i]) (i = range(1, k+1))
#https://stackoverflow.com/questions/31960583/efficiency-of-pythons-itertools-product
#256ms, 158B, BUT 99840 KB -> import를 product만 하면 236ms에 99836KB
#이거보고 combination도 잠깐 combination만 import 해서 실험해봤으나 실행시간은 똑같이 76ms, 메모리도 똑같음(세 버전 모두).
#아마 product 로직 내에서 2차원 배열 같은 걸 쓰고 있어서 메모리를 많이 잡아 먹고 있고
#함수만 뽑아서 import하는 건 메모리와 실행 시간에 큰 영향을 주지 않는 것으로 보임.

from itertools import product

end, num = map(int, input().split())
print('\n'.join(list(map(' '.join, product(map(str, list(range(1, end+1))), repeat = num)))))