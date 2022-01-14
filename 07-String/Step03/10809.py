#BOJ 10809
import string

word = input()

alph_lower = list(string.ascii_lowercase)
pos = 0
res = ""
for i in alph_lower:
    pos = word.find(i)
    res = res + str(pos) + " "
print (res.rstrip())