s = input()
L = list(s)
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in croatia:
    s = s.replace(a, '0')

print(len(s))
