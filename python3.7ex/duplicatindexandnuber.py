l=[1,3,5,3,7,8,0,2,3,5]
len=len(l)
i=0
while(i<len):
    j=i+1
    while(j<len):
        if l[i]==l[j]:
            print("duplicate num in list",l[j])
            print("duplicate index  a number",j)
            del l[j]
            len=len-1
        j=j+1
    i=i+1
print("element after dulicate num is delete:",l)
    
