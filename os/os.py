import os, shutil
print(os.getcwd())
# os.mkdir('extra')
print(os.path.exists('extra'))
# open('extra', 'a').close()
os.chdir('e:/Practice/python/practice/os')
print(os.getcwd())
print(os.listdir('e:/Practice/python/practice/os/extra'))
dir = os.listdir()
path = os.getcwd()
for item in dir:
    shutil.move(item,os.path.join(path,f'Images\{item}'))
Dir = os.walk(os.getcwd())
for current_path,folders,files in Dir:
    print(f'curren_folder : {current_path}')
    print(f'folders : {folders}')
    print(f'files : {files}')

os.chdir('e:/Practice/python/practice/os/extra')
# shutil.rmtree('X')




