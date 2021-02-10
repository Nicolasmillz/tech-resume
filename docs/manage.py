from utils import *
import sys

print('''Usage: 
    Rebuild site:    python manage.py build
    Create new page: python manage.py new''')
prompt = input('Please choose a command: ')

if prompt == 'python manage.py build':
    main()
elif prompt == 'python manage.py new':
    create_new()
else:
    print("Neither command chosen. Run 'manage.py' file again if you would like to build or create new file.")