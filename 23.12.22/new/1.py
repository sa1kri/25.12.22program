import random
w=1
while w==1:
    b=int(input("Количество букв: "))
    s=int(input("Количество слов: "))
    if b>0 and b%2==1 and s>0:
        w-=1
    else:
        print("Ошибка.")
a='eyuioa'
q="qwrtpsdfghjklzxcvbnm"
r=''
for i in range(0, s):
    k=1
    for i in range(0, b):
        if k%2==0:
            r+=random.choice(a)
        else:
            r+=random.choice(q)
        k+=1
    r+=", "
r=r[:-2]
r+="."
print(r)