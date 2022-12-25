mylist = []
a = [1,2,3,4,5,6]
b = [9,8,7,6]
for x in range(max(len(a), len(b))):
    if x < len(a):
        mylist.append(a[x])
    if x < len(b):
        mylist.append(b[x])