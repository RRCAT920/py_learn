import shutil

shutil.copyfileobj(open('random_.py'), open('random_2.py', 'w'))

shutil.copyfile('random_.py', 'random_3.py')