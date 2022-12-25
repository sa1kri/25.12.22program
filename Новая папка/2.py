i=[]
a=[1,2,3,4]
b=['s','f','g']
i.extend(a)
i.extend(b)
print(i)

def up():
    mylist = []
    for x in range(max(len(a), len(b),)):
        if x < len(a):
            mylist.append(a[x])
        if x < len(b):
            mylist.append(b[x])
        
        print(mylist)
up()
