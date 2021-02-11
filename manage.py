from utils import *
import sys

print('''Usage: 
    Rebuild site:    python manage.py build
    Create new page: python manage.py new''')
prompt = sys.argv[1]

if prompt == 'build':
    main()
elif prompt == 'new':
    create_new()
else:
    print("Neither command chosen. Run 'manage.py' file again if you would like to build or create new file.")