# Designer avec multipage en tete pour chaque type d'operation differente

import random

def generate_random_num(n):
    return random.randrange(n)

def generate_random_num_digits(digits):
    if (digits == 1):
        return random.randrange(1, 10)
    elif (digits == 2):
        return random.randrange(10, 99)
    else:
        return random.randrange(100, 1000)
    

