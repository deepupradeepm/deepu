def one(n):
    l=[1,2,3,4]
    print(l)
    print([i*i for i in l])
    return n
@one
def display():
    print("this display")
    

display()
