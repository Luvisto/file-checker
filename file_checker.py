#THis is an example script where we check if the file exist or not
import os

h=input('Enter a file you are looking for: ')
if os.path.exists(f'{h}'):
    print('There is such file')
else:
    print('There is no file that has that name')