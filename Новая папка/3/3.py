string = 'zzeennrrrss'
b = sorted(string)
print (b)

def fix(b):
    s = set()
    list = []
    for ch in b:
        if ch not in s:
            s.add(ch)
            list.append(ch)
    
    return ''.join(list)        


print(fix(b))

bdd=sorted(fix(b))
print(bdd)