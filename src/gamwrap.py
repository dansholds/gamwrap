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

def update_calendar():
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def email_validation(answers, current):
        if not re.match(regex, current):
            raise errors.ValidationError('', reason='I don\'t like thats users email!')

        return True

    questions = [
        inquirer.Text('calendar',
                    message="What's the calendar?",
                    validate=email_validation,
        ),
        inquirer.Text('user',
                    message="What's the users email",
                    validate=email_validation,
                    )
    ]
    answers = inquirer.prompt(questions)
    print("gam calendar {} add editor {}".format(answers['calendar'], answers['user']))

def main():
    welcome()
    check()
    gam_menu()

if __name__ == "__main__":
    main()