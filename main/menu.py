#!/usr/bin/env python3
# Import build in modules
from colorama import Fore, Style # built-in colorama module: black, red, green, yellow, blue, magenta, cyan, and white
from colorama import init
init(autoreset=True) # Reset colors in new line

# Import own modules
from modules import cls

# Text generated with https://patorjk.com/software/taag/#p=display&f=Soft&t=PyPlate
title ="""                                                  
    ,------.          ,------. ,--.          ,--.          
    |  .--. ',--. ,--.|  .--. '|  | ,--,--.,-'  '-. ,---.  
    |  '--' | \  '  / |  '--' ||  |' ,-.  |'-.  .-'| .-. : 
    |  | --'   \   '  |  | --' |  |\ '-'  |  |  |  \   --. 
    `--'     .-'  /   `--'     `--' `--`--'  `--'   `----' 
             `---'                                         
                            v{version} by Thomas P. Jørgensen, tpnet.dk 2023\n\n""".format(version='1.1')

help ="""
 === HELP ===
 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ac turpis egestas sed tempus urna et pharetra pharetra. Nibh mauris cursus mattis molestie a iaculis.
 Scelerisque in dictum non consectetur a erat nam at lectus. Amet commodo nulla facilisi nullam vehicula ipsum a.\n
 Vel facilisis volutpat est velit egestas dui id ornare. Ut etiam sit amet nisl purus in mollis nunc sed. Ut tristique et egestas quis.
 Purus semper eget duis at tellus at urna condimentum. Dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida.
 Eget duis at tellus at urna condimentum mattis pellentesque. Nec feugiat nisl pretium fusce id velit ut tortor.
 At tellus at urna condimentum mattis pellentesque id nibh. Curabitur gravida arcu ac tortor dignissim convallis aenean.

 === Tips & Tricks ===
 * Phasellus in quam volutpat sapien vehicula malesuada id sed diam.
 * In non quam facilisis, pretium enim ac, ultrices dolor.
 * Vivamus vel purus id nisi vehicula lobortis vel a dolor.
 * Quisque pellentesque orci sed convallis suscipit.
 * Nunc volutpat nulla ut sapien vulputate tincidunt.
"""
                            
def main_menu():
    while True:
        cls() # Clear the screen
        print(Fore.CYAN + title)
        print(' === Main menu ===')
        print(' {}[1]{}: Option 1'.format(Fore.MAGENTA,Style.RESET_ALL))
        print(' {}[2]{}: Option 2'.format(Fore.MAGENTA,Style.RESET_ALL))
        print(' {}[S]{}: System Information'.format(Fore.MAGENTA,Style.RESET_ALL))
        print(' {}[H]{}: Help'.format(Fore.MAGENTA,Style.RESET_ALL))
        print(' {}[Q]{}: Quit'.format(Fore.MAGENTA,Style.RESET_ALL))

        choice = input('\n Enter your choice & hit {}<Enter>{} :'.format(Fore.MAGENTA,Style.RESET_ALL ))

        # 1: Option 1
        if choice == "1":
            submenu1()
            
        # 2: Option 2
        elif choice == "2":
            submenu2()
            
        # S: System Information
        elif choice.lower() == "s":
            print('\n === System Information ===')
            import sys
            import platform

            required_version = "3.10.0"
            current_version = sys.version_info

            if current_version >= (3, 10, 0):
                print('\nSystem running Python version {} (Required minimum version is {}).'.format(platform.python_version(), required_version))
                print('\nrequirements.txt:')
                with open('requirements.txt', 'r') as f:
                    contents = f.read()
                    print('* ',contents)
                input('\nTo return to main menu hit {}<Enter>'.format(Fore.MAGENTA))
            else:                
                print(' \n{}{}Python version is below required version & full functionallity cannot be garantied.\nPlease upgrade to version {} or higher.\n'.format(Style.BRIGHT, Fore.RED, required_version))
                print('\nrequirements.txt:')
                with open('requirements.txt', 'r') as f:
                    contents = f.read()
                    print('* ',contents)
                input('\nTo return to main menu hit {}<Enter>'.format(Fore.MAGENTA))
        
        # H: Help
        elif choice.lower() == "h":
            print(Fore.WHITE + help)
            input('\nTo return to main menu hit {}<Enter>'.format(Fore.MAGENTA))
        
        # Q: Quit
        elif choice.lower() == "q":
            print(Fore.CYAN + "\n\t Goodbye...\n")
            break
        
        # User entered invalid choice
        else:
            #cls()  # Clear the screen
            print(' {}{}Option {} is not valid\n'.format(Style.BRIGHT, Fore.RED, choice))
            input('\nTo return to main menu hit {}<Enter>'.format(Fore.MAGENTA))




### Submeny definitions below #############################
def submenu1():
    while True:
        print('\n === Sub menu 1 ===')
        print(' {}[1]{}: Option 1.1'.format(Fore.MAGENTA, Style.RESET_ALL))
        print(' {}[2]{}: Option 1.2'.format(Fore.MAGENTA, Style.RESET_ALL))
        print(' {}[B]{}: Back'.format(Fore.MAGENTA, Style.RESET_ALL))
        
        choice = input('\n Enter your choice & hit {}<Enter>{} :'.format(Fore.MAGENTA, Style.RESET_ALL))

        if choice == "1":
            print('\n Option 1.1')
            input('\nTo return to {}Sub Menu 1{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            # Returning to Sub menu 1
        
        elif choice == "2":
            print('\n Option 1.2')
            input('\nTo return to {}Main Menu{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            main_menu() # Returning to the main menu
        
        elif choice.lower() == "b":
            print("Returning to main menu...")
            break
        
        else:
            print(' {}{}Option {} is not valid\n'.format(Style.BRIGHT, Fore.RED, choice))

def submenu2():
    while True:
        print('\n === Sub menu 2 ===')
        print(' {}[1]{}: Option 2.1'.format(Fore.MAGENTA, Style.RESET_ALL))
        print(' {}[2]{}: Option 2.2'.format(Fore.MAGENTA, Style.RESET_ALL))
        print(' {}[B]{}: Back'.format(Fore.MAGENTA, Style.RESET_ALL))
        
        choice = input('\n Enter your choice & hit {}<Enter>{} :'.format(Fore.MAGENTA, Style.RESET_ALL))

        if choice == "1":
            print('\n Option 2.1')
            input('\nTo return to {}Sub Menu 1{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            # Returning to Sub menu 2
        
        elif choice == "2":
            print('\n Option 2.2')
            input('\nTo return to {}Main Menu{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            main_menu() # Returning to the main menu
        
        elif choice.lower() == "b":
            print("Returning to main menu...")
            break
        
        else:
            print(' {}{}Option {} is not valid\n'.format(Style.BRIGHT, Fore.RED, choice))
