n1 = int(input("Введите целое число из 4 чисел: "))
def gof():
    x = [int(a) for a in str(n1)]
    print(x)
    a=len(x)
    f=int(a/2)
    print(" ")
    #print(f)
    d=f-1
    i=0
    while i < f:
        print(x[d])
        i+=1
        d=d-1
    while i < a:
        print(x[f])
        i+=1
        f+=1
gof()

