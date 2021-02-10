from utils import *

print('''Usage: 
    Rebuild site:    python manage.py build
    Create new page: python manage.py new''')
prompt = input('Please choose a command: ')

if prompt == 'python manage.py build':
    main()
elif prompt == 'python manage.py new':
    #function to build new page
    main()
else:
    print("Neither command chosen. Run 'manage.py' file again if you would like to build or create new file.")
