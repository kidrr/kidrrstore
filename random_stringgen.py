# Generates custom number of strings with randon chars and numbers

import random, string
def random_chars(a):
    chars = string.letters + string.digits
    s = [random.choice(chars) for i in range(a)]
    output = (''.join(s) + '\n')
    return output

how_many = input("How many strings: ")
how_long = input("How long should the string be in chars: ")

for i in range(how_many):
    result = random_chars(how_long)
    print result

