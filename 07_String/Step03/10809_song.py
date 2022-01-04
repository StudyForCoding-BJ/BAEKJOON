s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
arr = [0] * 26

for i in range(0, 26):
    arr[i] = s.find(alphabet[i])


for a in arr:
    print(a, end=' ')
