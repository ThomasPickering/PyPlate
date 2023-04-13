#!/usr/bin/env python3
# Import build in modules
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