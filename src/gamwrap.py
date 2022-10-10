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
    sleep(1)
    if not os.path.isfile('/Users/'+ os.environ.get('USER') +'/bin/gam/gam'):
        print('GAM is not installed. Please install it first.')
        sys.exit(1)
    else:
        print('GAM is installed.')
        sleep(1)

def return_to_main():
    questions = [
        inquirer.Confirm('return_to_menu',
                    message="Return to main menu?"),
    ]
    answers = inquirer.prompt(questions)
    if answers['return_to_menu'] == True:
        gam_menu()
    else:
        print("exiting...")
        sys.exit(1)

def gam_menu():
    questions = [
        inquirer.List('menu',
                    message="What GAM option do you want?",
                    choices=['Calendar', 'Users', 'Groups', 'Drive', 'Exit'],
                ),
    ]

    answers = inquirer.prompt(questions)
    if answers['menu'] == 'Calendar':
        calendar_menu()
    elif answers['menu'] == 'Exit':
        print("exiting...")
        sys.exit(1)
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
    answers = inquirer.prompt(questions)

    # function for updating calendar
    def cal_update(opt):
        opt=opt.lower()
        update_questions = [
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
        update_answers = inquirer.prompt(update_questions)
        confirm = [
            inquirer.Confirm('confirm_' + opt,
                        message="Are you sure you want to make {} a {} of {}?".format(update_answers['user'], opt, update_answers['calendar'])),
        ]
        confirm_answers = inquirer.prompt(confirm)
        # If they confirm, make the change
        if confirm_answers['confirm_' + opt] == True:
            print("Making {} a {} of {}".format(update_answers['user'], opt, update_answers['calendar']))
            print("gam calendar {} add {} {}".format(update_answers['calendar'], opt, update_answers['user']))
            sleep(2)
            return_to_main()
        else:
            return_to_main()

    # call cal_update function with the option the user selected
    cal_update(opt=answers['calendar_menu'])

def main():
    welcome()
    check()
    gam_menu()

if __name__ == "__main__":
    main()
