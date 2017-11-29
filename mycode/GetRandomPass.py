from random import choice
import string

def GenPassword(length=8,chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

for i in range(1):
    print(GenPassword(8))