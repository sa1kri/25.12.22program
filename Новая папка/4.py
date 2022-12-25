import string 
import random 
def id_generator(size=6, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))
id_generator() '6793YUIO'
id_generator(3, "6793YUIO") 'Y3U' 
string.ascii_uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
string.digits '0123456789' 
string.ascii_uppercase + string.digits 'NMJLLHFLFT' range(4) # range create a list of 'n' numbers [0, 1, 2, 3]
['elem' for _ in range(4)] # we use range to create 4 times 'elem' ['elem', 'elem', 'elem', 'elem']  
    random.choice("abcde") 'a' 
    random.choice("abcde") 'd'
    .choice("abcde") 'b' 
[random.choice('abcde') for _ in range(3)] ['a', 'b', 'b'] 
[random.choice('abcde') for _ in range(3)] ['e', 'b', 'e'] 
[random.choice('abcde') for _ in range(3)] ['d', 'a', 'c'] 
''.join(['a', 'b', 'b']) 
[random.choice('abcde') for _ in range(3)] ['d', 'c', 'b'] 
''.join(random.choice('abcde') for _ in range(3))  
