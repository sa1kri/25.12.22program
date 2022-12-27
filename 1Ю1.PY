



def gof(n1):
    x = [int(a) for a in str(n1)]
    print(x)
    a=len(x)
    
    f=int(a/2)
    t=a%2 
  
    
    if t<=0:
        one=(x[:f])
        two=(x[f:])
        re_o=list(reversed(one))
        re_t=list(reversed(two))
        sum=re_o+re_t
        god=''.join(map(str,sum))
        print(god)
    else:
        mib=x[0]
        x.remove(mib)
        one=(x[:f])
        two=(x[f:])
        re_o=list(reversed(one))
        re_t=list(reversed(two))
        sum=re_o+re_t
        god=''.join(map(str,sum))
        
        print(god,mib)
        
        
    
n1 = int(input("Введите целое число из 4 чисел: "))    
gof(n1)

n2 = 0
while n1 > 0:
   
    digit = n1 % 10
    
    n1 = n1 // 10
    
    n2 = n2 * 10
   
    n2 = n2 + digit  
 
print('"Обратное" ему число:', n2)
