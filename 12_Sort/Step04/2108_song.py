import sys

N = int(sys.stdin.readline())

read = []
for i in range(N):
    read.append(int(sys.stdin.readline()))

read.sort()

#카운팅소트
fine = [0] * 8001
for i in read:
    fine[i+4000] += 1
    

#산술평균    
print(round(sum(read)/N))

#중앙값
print(read[N // 2])


#최빈값
n = max(fine)
m = fine.index(n)

fine[m] = 0 #가장 큰 최빈값 없앰
if max(fine) == n:
    m = fine.index(max(fine))

print(m-4000)

#범위
print(max(read) - min(read))
