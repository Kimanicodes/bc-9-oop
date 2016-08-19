import os
from notes_application import NotesApplication

os.system('clear')


def display_menu():
    print """
    CHOOSE OPTION FROM MENU
    1. Enter Author Name
    2. Creat a New Note
    3. List all your Notes
    4. Get a particluar List
    5. Search Text within your notes list
    6. Edit a Particular Note
    7. Quit
    """
display_menu()
var = raw_input('\n')

if int(var) == 1:
    name = raw_input('Enter Author Name:\n')
    name = str(name)
    x = NotesApplication(name)
    print('Welcome %s' % x.author)
    print('What Would You like to Do?')
    display_menu()

elif int(var) == 2:
    create_note = raw_input('Create Your Note:\n')
    create_note = str(create_note)
    x.create(create_note)
    display_menu()

elif int(var) == 3:
    x.list()

elif int(var) == 4:
    get_note = raw_input('Enter Note ID:\n')
    get_note = int(get_note)
    x.get(get_note)