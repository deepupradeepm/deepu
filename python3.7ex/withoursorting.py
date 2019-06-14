l=[10,2,4,3,6,7,9,8]
for y in range(len(l)-1):
    for x in range(len(l)-1):
      if l[x]>l[x+1]:
        l[x],l[x+1]=l[x+1],l[x]

print(l)
