list=[10,20,30,40,1,2,3]
for y in range(len(list)-1):
  for x  in range(len(list)-1):
    if list[x]>list[x+1]:
        list[x],list[x+1]=list[x+1],list[x]

print(list)
