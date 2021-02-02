import string
from random import sample

population = string.ascii_letters + string.digits + string.punctuation
print(''.join(sample(population, 16)))