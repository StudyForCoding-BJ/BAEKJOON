#BOJ 2941

tstWord = input()

# First, exclude dz=, lj, nj. This is absolutely croatian alph
tmplist = ["lj", "nj", "dz=", "c=", "c-", "d-", "s=", "z="]
for i in tmplist:
    if tstWord.find(i) != -1:
        tstWord = tstWord.replace(i, "0")

print (len(tstWord))