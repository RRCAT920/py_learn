import zipfile

with zipfile.ZipFile('cannot_cpdir2.zip', 'w') as fout:
    fout.write('shutil_.py')
    fout.write('random_.py')
    fout.write('cannot_cpdir/')

# with zipfile.ZipFile('zipfile_package.zip') as fin:
#     fin.extractall()