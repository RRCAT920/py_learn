import string
from random import sample

print(''.join(sample(string.ascii_lowercase + string.digits, 5)))