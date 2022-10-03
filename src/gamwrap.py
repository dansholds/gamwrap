# -*- coding: utf-8 -*-

import os
from secrets import choice
import sys
import subprocess
from time import sleep
import inquirer
from inquirer import errors
from pprint import pprint
import re


os.environ['USER'] = 'username'

_EXIT_WORDS = ["quit", "exit", "leave"]

#--------------------------------------------
def welcome():
    print(r"""                                                                             
                                     ____                                            ,-.----.    
  ,----..      ,---,               ,'  , `.           .---.,-.----.      ,---,       \    /  \   
 /   /   \    '  .' \           ,-+-,.' _ |          /. ./|\    /  \    '  .' \      |   :    \  
|   :     :  /  ;    '.      ,-+-. ;   , ||      .--'.  ' ;;   :    \  /  ;    '.    |   |  .\ : 
.   |  ;. / :  :       \    ,--.'|'   |  ;|     /__./ \ : ||   | .\ : :  :       \   .   :  |: | 
.   ; /--`  :  |   /\   \  |   |  ,', |  ': .--'.  '   \' ..   : |: | :  |   /\   \  |   |   \ : 
;   | ;  __ |  :  ' ;.   : |   | /  | |  ||/___/ \ |    ' '|   |  \ : |  :  ' ;.   : |   : .   / 
|   : |.' .'|  |  ;/  \   \'   | :  | :  |,;   \  \;      :|   : .  / |  |  ;/  \   \;   | |`-'  
.   | '_.' :'  :  | \  \ ,';   . |  ; |--'  \   ;  `      |;   | |  \ '  :  | \  \ ,'|   | ;     
'   ; : \  ||  |  '  '--'  |   : |  | ,      .   \    .\  ;|   | ;\  \|  |  '  '--'  :   ' |     
'   | '/  .'|  :  :        |   : '  |/        \   \   ' \ |:   ' | \.'|  :  :        :   : :     
|   :    /  |  | ,'        ;   | |`-'          :   '  |--" :   : :-'  |  | ,'        |   | :     
 \   \ .'   `--''          |   ;/               \   \ ;    |   |.'    `--''          `---'.|     
  `---`                    '---'                 '---"     `---'                       `---`     
                                                                                                 
                """)

def check():
    print("Checking if gam is installed...")
    sleep(2)
    if not os.path.isfile('/Users/dholdsworth/bin/gam/gam'):
        print('GAM is not installed. Please install it first.')
        sys.exit(1)
    else:
        print('GAM is installed.')
        sleep(2)

def return_to_main():
    questions = [
        inquirer.Confirm('return_to_menu',
                    message="Return to main menu?"),
    ]
    answers = inquirer.prompt(questions)
    if answers['return_to_menu'] == True:
        gam_menu()
    else:
        print("Exiting...")
        exit(1)

def gam_menu():
    questions = [
        inquirer.List('menu',
                    message="What GAM option do you want?",
                    choices=['Calendar', 'Users', 'Groups', 'Drive'],
                ),
    ]

    answers = inquirer.prompt(questions)
    if answers['menu'] == 'Calendar':
        calendar_menu()
    else:
        print("Not implemented yet")
        return_to_main()

def calendar_menu():
    questions = [
        inquirer.List('calendar_menu',
                    message="What GAM Calendar option do you want?",
                    choices=['Create', 'Update', 'Delete'],
                ),
    ]

    answers = inquirer.prompt(questions)
    if answers['calendar_menu'] == 'Update':
        update_calendar()
    else:
        print("Not implemented yet")
        return_to_main()

def update_calendar():
    # Regex and function to validate email addresses
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    def email_validation(editor_answers, current):
        if not re.match(regex, current):
            raise errors.ValidationError('', reason='I don\'t like thats users email!')

        return True

    # Ask the user if they want to update read, editor or owner of calendar
    questions = [
        inquirer.List('calendar_menu',
                    message="What update do you want to make?",
                    choices=['Read', 'Editor', 'Owner'],
                ),
    ]

    # Start logic to pivot between different options
    answers = inquirer.prompt(questions)
    if answers['calendar_menu'] == 'Editor':
        # Ask user for calander and user
        editor_questions = [
            inquirer.Text('calendar',
                        message="What's the calendar?",
                        validate=email_validation,
            ),
            inquirer.Text('user',
                        message="What's the users email",
                        validate=email_validation,
                        )
        ]
        # Confirm with user that they want to make the change
        editor_answers = inquirer.prompt(editor_questions)
        confirm = [
            inquirer.Confirm('confirm_editor',
                        message="Are you sure you want to make {} an editor of {}?".format(editor_answers['user'], editor_answers['calendar'])),
        ]
        confirm_answers = inquirer.prompt(confirm)
        # If they confirm, make the change
        if confirm_answers['confirm_editor'] == True:
            print("Making {} an editor of {}".format(editor_answers['user'], editor_answers['calendar']))
            print("gam calendar {} add editor {}".format(editor_answers['calendar'], editor_answers['user']))
            sleep(2)
            return_to_main()
        else:
            print("Returning to main menu")
            gam_menu()
    # If they pick anything other than Update it will ask to return to the main menu
    else:
        print("Not implemented yet")
        return_to_main()

def main():
    welcome()
    check()
    gam_menu()

if __name__ == "__main__":
    main()
