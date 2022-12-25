import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand = ''.join(random.choice(letters) for i in range(length))
    result = "".join(dict.fromkeys(rand))
    print("Рандомное слово из количества букв", length, "это:", rand)
    print("Вот что получилось:",result)
generate_random_string(10)




