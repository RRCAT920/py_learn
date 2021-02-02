import tarfile

with tarfile.open('egg.tar', 'w') as fout:
    fout.add('zip_.py')
    fout.add('racelamp.py')

with tarfile.open('egg.tar') as fin:
    fin.extractall('./egg')