import os
import shutil

dirName = input('Enter folder name: ')
# dirName = 'test'
files = os.listdir(dirName)
print(files)
for file in files:
    fileName, extension = file.split('.')
    print(fileName, extension)
    if extension == '':
        continue
    if os.path.exists(dirName + '/' + extension):
        shutil.move(dirName+'/' + file, dirName + '/' + extension + '/' + file)
    else:
        os.makedirs(dirName + '/' + extension)
        shutil.move(dirName+'/' + file, dirName + '/' + extension + '/' + file)
