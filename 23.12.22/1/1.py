import random
import string

s = int(input("ведите голичество букв: "))

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)


generate_random_string(s)



s=input("ведите слова: ")
print('Слово является палиндромом' if s == s[::-1] else 'Слово не является палиндромом')