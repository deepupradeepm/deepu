l=[1,3,4,56,2,3,4]
len=len(l)
i=0
while i<len:
    j=i+1
    while j<len:
        if l[i]==l[j]:
            print("duplicate index of a number:",j)
            print("duplicate number in list",l[j])
            
            del l[j]
            len=len-1
        j=j+1
    i=i+1
print("list without duplicate number",l)
                  
