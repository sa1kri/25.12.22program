import time
u=1
while u==1:
    q=int(input("Длина строки: "))-1
    if q>0:
        u-=1
    else:
        print("Нужно число больше 1.")
w=input("Символ: ")
e=1
while e==1:
    r=0
    for i in range(q):
        t=r
        y=q-r
        rint("|",t*" ",w,y*" ","|",end="\r")
        time.sleep(0.1)
        r+=1
    r=0
    for i in range(q):
        t=q-r
        y=r
        print("|",t*" ",w,y*" ","|",end="\r")
        time.sleep(0.1)
        r+=1 