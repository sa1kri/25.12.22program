import time
s=1
while s==1:
    q=int(input("Длина строки: "))
    u=int(input("Количество строк: "))
    if q>1 and u>1:
        s-=1
    else:
        print("Нужно число больше 1.")
w=input("Символ: ")
e=1
while e==1:
    r=0
    a=0
    f=0
    g=0
    for i in range(u):
        for i in range(q):
            d=0
            t=r
            y=q-r
            o=a+g
            p=u-a-g-1
            print("")
            for i in range(o):
                print("|",t*" "," ",y*" ","|")
            print("|",t*" ",w,y*" ","|")
            for i in range(p):
                print("|",t*" "," ",y*" ","|")
            print("")
            time.sleep(0.2)
            if f%2==0:
                r+=1
            else:
                r-=1
        g+=1
        f+=1
    r=0
    a=0
    f=0
    g=0
    for i in range(u):
        for i in range(q):
            d=0
            y=r
            t=q-r
            p=a+g
            o=u-a-g-1
            print("")
            for i in range(o):
                print("|",t*" "," ",y*" ","|")
            print("|",t*" ",w,y*" ","|")
            for i in range(p):
                print("|",t*" "," ",y*" ","|")
            print("")
            time.sleep(0.2)
            if f%2==0:
                r+=1
            else:
                r-=1
        g+=1
        f+=1    