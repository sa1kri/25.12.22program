a=int(input("первое число: "))
w=int(input("второе число: "))
s=int(input("третье число: "))
d=int(input("четвертое число: "))

i=0

if a<=w: #1
    if w<=s: #2
        if s<=d: #3
            print("#"*d)
            print("#"*s)
            print("#"*w)
            print("#"*a)
        elif d<s: #3
            print("#"*s)
            print("#"*d)
            print("#"*w)
            print("#"*a)
            
    elif s<w: #2
        if w<=d: #4
            print("#"*d)
            print("#"*w)
            print("#"*s)
            print("#"*a)
        elif d<w: #4
            print("#"*w)
            print("#"*d)
            print("#"*s)
            print("#"*a)
            
elif w<a: #1
    if a<=s: #5
        if s<=d: #6
            print("#"*d)
            print("#"*s)
            print("#"*a)
            print("#"*w)
        elif d<s: #6
            print("#"*s)
            print("#"*d)
            print("#"*a)
            print("#"*w)
            
    elif s<a: #5 
        if a<=d: #7
            print("#"*d)
            print("#"*a)
            print("#"*s)
            print("#"*w)
        elif d<a: #7
            print("#"*a)
            print("#"*d)
            print("#"*s)
            print("#"*w)