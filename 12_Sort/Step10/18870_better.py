#BOJ 18870_better

size = int(input())

#int로 mapping 후 바로 list화
intlist = list(map(int, input().split()))

#sort() vs. sorted() -> return 여부
sortedlist = sorted(list(set(intlist)))

#출력 개선
for i in intlist:
    print (sortedlist[i])