s="aba"
revstr=""
for x in s:
    revstr=x+revstr
print("reverse of a str",revstr)
if s==revstr:
    print("polyndrome")
else:
    print("not polyndrome")
