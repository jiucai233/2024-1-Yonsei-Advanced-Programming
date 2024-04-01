import os
currentwd=os.getcwd()
print(f'current working directory:{currentwd}')
os.chdir('..')
currentwd=os.getcwd()
print(f'current working directory:{currentwd}')
listdir=os.listdir()
print(listdir)