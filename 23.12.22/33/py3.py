"""
def sort(a):
    for i in range(0,len(a)-1): 
        for j in range(len(a)-1): 
            if(a[j]>a[j+1]): 
                temp = a[j] 
                a[j] = a[j+1] 
                a[j+1] = temp 
    return a

a = [i for i in input()]
print(sort(a))
"""

def sort(a):
    for i in range(0,len(a)-1): 
        for j in range(len(a)-1): 
            if a[j]>a[j+1]: 
                temp = a[j] 
                a[j] = a[j+1] 
                a[j+1] = temp
    
    return a

a = [i for i in input()]
print(sort(a))