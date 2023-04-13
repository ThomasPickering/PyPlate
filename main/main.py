#!/usr/bin/env python3
# Import build in modules

"""
PyPlate is an attempt to make a python boilerplate. The boilderplate includes:

    === Main menu ===
    [1]: Option 1
            === Sub menu 1 ===
            [1]: Option 1.1
            [2]: Option 1.2
            [B]: Back
    [2]: Option 2
             === Sub menu 2 ===
            [1]: Option 2.1
            [2]: Option 2.2
            [B]: Back
    [S]: System Information
            Python version
            Requirements
    [H]: Help
            Print Help + Tips & Tricks
    [Q]: Quit
            Exit program/script
            
Please notice, that there are 2 way 2 navigate back to the main menu:
    * Choice 1 returns to the sub menu
    * Choise 2 returns direcly to the main menu

        if choice == "1":
            print('\n Option 1.1')
            input('\nTo return to {}Sub Menu 1{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            # Returning to Sub menu 1
        
        elif choice == "2":
            print('\n Option 1.2')
            input('\nTo return to {}Main Menu{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            main_menu() # Returning to the main menu
            
Read more:
https://pypi.org/project/colorama/


Have fun!

Thomas P.
"""
    

import os
from colorama import Fore, Style # built-in colorama module: black, red, green, yellow, blue, magenta, cyan, and white
from colorama import init
init(autoreset=True) # Reset colors in new line

# Import own modules
from modules import cls
from menu import main_menu

# The main script
def main():
    # The main menu
    main_menu()

if __name__ == "__main__":
    # Clear the screen
    cls()
    #Execute the main definition
    main()

else:
    # Do nothing so far
    pass