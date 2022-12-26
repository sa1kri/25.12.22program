t=1
while t>0:
    q=int(input("Первое число: "))
    w=int(input("Второе число: "))
    e=int(input("Третие число: "))
    r=int(input("Четвёртое число: "))
    if q>=0 and w>=0 and e>=0 and r>=0:
        t-=1
    else:
        print("Нужно положительные числа или 0.")
o=1
while o>0:
    y=int(input("Не меняется-0; Возрастание-1; Убывание-2: "))
    if y==0 or y==1 or y==2:
        o-=1
        if y==0:
            print(q*"#","-",q)
            print(w*"#","-",w)
            print(e*"#","-",e)
            print(r*"#","-",r)
        elif y==1:
            u=[q,w,e,r]
            u.sort()
            print(u[0]*"#","-",u[0])
            print(u[1]*"#","-",u[1])
            print(u[2]*"#","-",u[2])
            print(u[3]*"#","-",u[3])
    else:
        u=[q,w,e,r]
        u.sort()
    u.reverse()
    print(u[0]*"#","-",u[0])
    print(u[1]*"#","-",u[1])
    print(u[2]*"#","-",u[2])
    print(u[3]*"#","-",u[3])