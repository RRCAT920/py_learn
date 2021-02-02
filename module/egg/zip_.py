import os
import zipfile

# with zipfile.ZipFile('cannot_cpdir2.zip', 'w') as fout:
#     fout.write('shutil_.py')
#     fout.write('random_.py')
#     for dirpath, dirnames, filenames in os.walk('cannot_cpdir'):
#         for filename in filenames:
#             fout.write(os.path.join(dirpath, filename))

with zipfile.ZipFile('cannot_cpdir2.zip') as fin:
    fin.extractall(path='./hello')